import re

access_log = open(f"{os.getcwd()}\\app\\access_log.txt", "r") #initilize access log
ipmap = {} #create hashmap to store IPs and keep track of if they're unique
uniqueiplist = [] #list that only stores unique IPs

for x in access_log:
    find = re.findall("(.*?)\s-", x) #use regex to find 
    ip_addr = find[0] #first element is the IP address
    if ip_addr not in ipmap:
        ipmap[ip_addr] = True #if IP address is not in the map already set it to true as unique
    else:
        ipmap[ip_addr] = False #if IP address is found again, set value to False

#iterate through IP map keys
for y in ipmap.keys():
    if ipmap[y] == True:
        uniqueiplist.append(y) #if hash value is True, that means it is a unique IP

print(uniqueiplist)