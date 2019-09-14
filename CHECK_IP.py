from netaddr import IPNetwork, IPAddress

filepath = 'blacklist.txt'
all_IP = []
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        all_IP.append(line.replace('\n', ''))
        line = fp.readline()
        cnt += 1

same_networks = dict()
for IP_line in all_IP:
    list_of_IP_in_network = []
    for other_IP in all_IP:
        network = other_IP.split("/")[0]
        if IPAddress(network) in IPNetwork(IP_line):
            list_of_IP_in_network.append(network)
    same_networks[IP_line] = list_of_IP_in_network

print(same_networks)

print(" Length o f Unique IP networks: " + str(len(same_networks)))
print(" Most IP's In a network: 4 ")
print("Most frequently accessed IP belonged to Holtzer.de a server hosting company")
print(" NAMP SCAN: " + str("nmap -sV 188.40.0.0 Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-13 22:26 CDT Nmap scan report for static.0.0.40.188.clients.your-server.de (188.40.0.0)Host is up (0.028s latency).Not shown: 996 filtered portsService detection performed. Please report any incorrect results at https://nmap.org/submit/ .Nmap done: 1 IP address (1 host up) scanned in 192.76 seconds"))




