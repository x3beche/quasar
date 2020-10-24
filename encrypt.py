import os

#functions
def banner():
    f=open("keyOperations\\banner", "r")
    print(f.read())
    f.close()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#key complier
banner()
keynum=input("Enter the number at the end of the key file : ")
clear()
fn="keyOperations\\key"+keynum
f=open(fn,"r")
klst=f.read().split(",")
f.close()
a=klst[0].split("-")
rtry=[[],[]]
for x in range(0,26):
    cache=klst[x].split("-")
    rtry[0].append(cache[0])
    rtry[1].append(cache[1])
    exec(rtry[1][x]+"=rtry[0][x]")
    cache.clear()
oW=rtry[1][ord(a[1])-65]
<<<<<<< Updated upstream
=======

def call(oW,nW):
    pass
>>>>>>> Stashed changes

def call(oW,nW):
    pass
    
#encrypt start
banner()
print("\n1-) Encrypt file (only txt files support)\n2-) Encrypt normal text\n")
obs=input("Option : ")
if int(obs)==1:
    pass
elif int(obs)==2:
    pass
else:
    print("Wrong option.")
