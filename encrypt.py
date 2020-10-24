import os

#KEY COMPLIER
f=open("keyOperations\\banner", "r")
print(f.read())
f.close()
keynum=input("Enter the number at the end of the key file : ")
os.system('cls' if os.name == 'nt' else 'clear')
fn="keyOperations\\key"+keynum
f=open(fn,"r")
klst=f.read().split(",")
f.close()
rtry=[[],[]]
for x in range(0,26):
    cache=klst[x].split("-")
    rtry[0].append(cache[0])
    rtry[1].append(cache[1])
    exec(rtry[1][x]+"=rtry[0][x]")
    cache.clear()

#ENCRYPT START
