import requests, json

BASE_URL = 'https://rat-api-v1.herokuapp.com/'

def getIps():
	url = BASE_URL + 'ips'
	myResponse = requests.get(url)

	if myResponse.ok:

		ips = []
	    ipsJson = json.loads(myResponse.content)

	    for ip in ipsJson:
		    ips.append(str(ip['ip']))

		return ips

	else:
	    myResponse.raise_for_status()

PORTS = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5005, 5900, 8000, 8080, 8443, 8888 ]

def check(ip):
	i = 0
	while not message_sent and i < len(PORTS):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto("Are you awake?", (ip, PORTS[i]))

		sock.bind((IP, PORTS[i]))
		data, addr = sock.recvfrom(1024)

		i+=1

	return message_sent

availableIps = []

for ip in getIps():
	if check(ip):
		availableIps.append(ip)

print availableIps