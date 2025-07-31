#list of private cidr blocks 
list_cidr = "192.168.34.0/24,10.4.120.0/22,172.20.48.0/20,100.72.0.0/16"
#set delimiter 
cidr = list_cidr.split(',')
#add each block to function
#range(len(cidr) go to the last block 
#the last block doesn't need a ','
for block in range(len(cidr)): 
    # format cidrmch("192.168.34.0/24", dstip)
    print(f"cidrmch(\"{cidr[block]}\", dstip), ", end="")
#get the last item 
last_block = len(cidr) - 1
#print the last item without the ','
print(f"cidrmch(\"{last_block}\", dstip)")
