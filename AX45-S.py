import os,time
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
    klst=f.read().split(",")
    for x in range(0,len(klst)):
        print(klst[x])
    f.close()


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
        g=0
        for z in range(0,len(rtry[0])):
            g=g+int(rtry[0][z])
        if g!= 351:
            print("Key file is missing or incorrect.")
            pause()
        stfb=False
    else:
        clear()
        banner()
        line()
        print("Key file not found, make sure key file is in main directory.")
        pause()


#encrypt algorithms
oW=rtry[1][ord(a[1])-65]
def f_encrypt(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own>nwn:
        chc=26-own+nwn
    else:
        chc=nwn-own
    return rtry[1][chc-1]
def f_decrypt(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own+nwn>26:
        chc=own+nwn-26
    else:
        chc=nwn+own
    return rtry[1][chc-1]



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
        final=""
        fnm=input("File Name » ")
        line()
        f=open(fnm+".txt","r")
        text=f.read().upper().replace(" ","").replace("\n","")
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
        banner()
        line()
        final=""
        text=input("Normal text » ").upper().replace(" ","")
        line()
        for y in range(0,len(text)):
            oW=f_encrypt(oW,text[y],rtry)
            final=final+oW
        print("Encrypted text »",final)
        line()
        pause()
    elif int(obs)==3:
        final=""
        text=input("Text » ").upper().replace(" ","")
        line()
        for y in range(0,len(text)):
            nW=text[y]
            final=final+f_decrypt(oW,nW,rtry)
            oW=text[y]
        print("Decrypted text:",final)
        line()
        pause()
    elif int(obs)==4:
        final=""
        fnm=input("File Name » ")
        line()
        f=open(fnm+".txt","r")
        text=f.read().upper().replace(" ","").replace("\n","")
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
        print("Wrong option.")
        pause()
