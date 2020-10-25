import os

#functions
def banner():
    f=open("keyOperations\\banner", "r")
    print(f.read())
    f.close()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def line():
    print("-----------------------------------------------------")
#key complier
banner()
line()
keynum=input("Enter the number at the end of the key file : ")
line()
#clear()
fn="keyOperations\\key"+keynum
fc = os.path.isfile(fn)
if fc==True:
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
else:
    clear()
    banner()
    print("Key file not found, make sure key file is in keyOperations directory.")
    exit()

#encrypt algorithm
oW=rtry[1][ord(a[1])-65]
final=""
def call(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own>nwn:
        chc=26-own+nwn
    else:
        chc=nwn-own
    return rtry[1][chc-1]

#ui start
#banner()
print("1-)Encrypt normal text\n2-)Encrypt file (only txt files support)")
line()
obs=input("Option » ")
line()
if int(obs)==2:
    pass
elif int(obs)==1:


    text=input("Text » ")
    text=text.upper()
    text=text.replace(" ","")
    line()
    for y in range(0,len(text)):
        #final.append(call(oW,text[y],rtry))
        oW=call(oW,text[y],rtry)
        final=final+oW

    print("Normal text:",text,"\nEncrypted text:",final)
    line()
else:
    print("Wrong option.")
