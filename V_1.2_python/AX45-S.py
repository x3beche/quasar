import os
import time


#functions
def banner():
    f=open("easy_command\\banner", "r")
    print(f.read())
    f.close()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress ENTER to do another action.")

def line():
    print("-----------------------------------------------------")

def opnr(data):
    print("\n")
    f = open(data, "r")
    klst=f.read().split("{")
    for x in range(0,len(klst)):
        cache=klst[x].split("}")
        print(cache[0],"-",cache[1])
        cache.clear()
    f.close()

def f_encrypt(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own>nwn:
        chc=34-own+nwn
    else:
        chc=nwn-own
    return rtry[1][chc-1]

def f_decrypt(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own+nwn>34:
        chc=own+nwn-34
    else:
        chc=nwn+own
    return rtry[1][chc-1]


#key complier
stfb=True
while stfb==True:
    clear()
    banner()
    line()
    keynum=input("Enter the number at the end of the key file : ")
    line()
    fn="key"+keynum+".ax"
    fc=os.path.isfile(fn)
    if fc==True:
        f=open(fn,"r")
        klst=f.read().replace("\n","").split("{")
        f.close()
        a=klst[0].split("}")
        rtry=[[],[]]
        for x in range(0,34):
            cache=klst[x].split("}")
            print(cache[0],cache[1])
            rtry[0].append(cache[0])
            rtry[1].append(cache[1])
            cache.clear()
        g=0
        for z in range(0,len(rtry[0])):
            g=g+int(rtry[0][z])
        if g!= 595:
            print("Key file is missing or incorrect.")
            pause()
        stfb=False
    else:
        clear()
        banner()
        line()
        print("Key file not found, make sure key file is in main directory.")
        pause()


#ui start
while True:
    clear()
    banner()
    line()
    print("1-)Encrypt normal text\n2-)Encrypt file (only txt files support)\n3-)Decrypt normal text\n4-)Decrypt file (only txt files support)\n5-)Key viewer")
    line()
    obs=input("Option » ")
    clear()
    if int(obs)==2:
        oW=rtry[1][ord(a[1])-65]
        banner()
        line()
        final=""
        fnm=input("File Name » ")
        line()
        f=open(fnm+".txt","r")
        text=f.read().upper().replace("\n","")
        f.close()
        for y in range(0,len(text)):
            oW=f_encrypt(oW,text[y],rtry)
            final=final+oW
        f = open(fnm+"_ax-en.txt", "a")
        f.write(final)
        f.close()
        print("Encryption process completed, %s_ax-en.txt created." %fnm)
        line()
        pause()
    elif int(obs)==1:
        oW=rtry[1][ord(a[1])-65]
        banner()
        line()
        final='"'
        text=input("Normal text » ").upper()
        line()
        for y in range(0,len(text)):
            oW=f_encrypt(oW,text[y],rtry)
            final=final+oW
        final=final+'"'
        print("Encrypted text »",final)
        line()
        pause()
    elif int(obs)==3:
        oW=rtry[1][ord(a[1])-65]
        banner()
        line()
        final=""
        text=input("Encrypted text » ").upper()
        line()
        for y in range(0,len(text)):
            nW=text[y]
            final=final+f_decrypt(oW,nW,rtry)
            oW=text[y]
        print("Decrypted text:",final)
        line()
        pause()
    elif int(obs)==4:
        oW=rtry[1][ord(a[1])-65]
        banner()
        line()
        final=""
        fnm=input("File Name » ")
        line()
        f=open(fnm+".txt","r")
        text=f.read().upper().replace("\n","")
        f.close()
        for y in range(0,len(text)):
            nW=text[y]
            final=final+f_decrypt(oW,nW,rtry)
            oW=text[y]
        f = open(fnm+"_ax-de.txt", "a")
        f.write(final)
        f.close()
        print("Encryption process completed, %s_ax-de.txt created." %fnm)
        line()
        pause()
    elif int(obs)==5:
        clear()
        banner()
        line()
        opnr(fn)
        print("\n")
        pause()
    else:
        banner()
        line()
        print("Wrong option.")
        pause()
