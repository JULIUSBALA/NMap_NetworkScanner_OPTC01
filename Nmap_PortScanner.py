import nmap 
ns = nmap.PortScanner() #initialize the nmap port scanner 
print(ns.nmap_version()) #printing the version og=f Nmap port version
ns.scan('127.0.0.1','1-65535',-v) # -Av gives all the information
print(ns.scaninfo())  #printing the scanned details

print(ns.csv()) # this is for scanned details with comma seprated
print(ns['127.0.0.2']).state()) # state of the network
print(ns['127.0.0.2']).all_protocols()) # protocols used on the network
print(ns['127.0.0.2']['tcp').keys()) # open ports on the network
print(ns['127.0.0.2']['tcp').has_tcp(80)) # check whether port 80 is open or not if open gives True other wise gives False