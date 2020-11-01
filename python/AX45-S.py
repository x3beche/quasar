import os
import time

#functions
def banner():
    f=open("easy_command/banner", "r")
    print(f.read())
    f.close()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    input("\nPress ENTER to turn main menu.")
def line():
    print("-----------------------------------------------------")
def opnr(data):
    print("\n")
    f = open(data, "r")
    klst=f.read().split("split")
    for x in range(0,len(klst)-1):
        cache=klst[x].split("axen")
        print(cache[0],"-",cache[1])
        cache.clear()
    f.close()

def f_encrypt(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own>nwn:
        chc=94-own+nwn
    else:
        chc=nwn-own
    return rtry[1][chc-1]

def f_decrypt(oW,nW,rtry):
    own=int(rtry[0][rtry[1].index(oW)])
    nwn=int(rtry[0][rtry[1].index(nW)])
    if own+nwn>94:
        chc=own+nwn-94
    else:
        chc=nwn+own
    return rtry[1][chc-1]

keyFiles=[]
with os.scandir('operationFiles/') as entries:
    for entry in entries:
        if entry.name[::-1][:2][::-1]=="ax":
            keyFiles.append(entry.name)


#key complier
stfb=True
while stfb==True:
    clear()
    banner()
    line()
    for q in range(0,len(keyFiles)):
        print(str(q+1)+"-)",keyFiles[q])
    line()
    keynum=input("Enter your key selection: » ")
    line()
    fn="operationFiles/"+keyFiles[int(keynum)-1]
    fc=os.path.isfile(fn)
    if fc==True:
        f=open(fn,"r")
        klst=f.read().replace("\n","").split("split")
        f.close()
        a=klst[0].split("axen")
        rtry=[[],[]]
        for x in range(0,94):
            cache=klst[x].split("axen")
            rtry[0].append(cache[0])
            rtry[1].append(cache[1])
            cache.clear()
        g=0
        for z in range(0,len(rtry[0])):
            g=g+int(rtry[0][z])
        if g!= 4465:
            print("Key file is missing or incorrect.")
            line()
            pause()
        stfb=False
    else:
        print("Key file not found, make sure key file is in keys-text directory.")
        line()
        pause()


#ui start
while True:
    clear()
    banner()
    line()
    print("1-)Encrypt normal text\n2-)Decrypt normal text\n3-)Encrypt file\n4-)Decrypt file\n5-)Key viewer")
    line()
    obs=input("Option » ")
    clear()
    if int(obs)==3:
        banner()
        line()
        textFiles=[]
        textFiles.clear()
        with os.scandir('operationFiles/') as entries:
            for entry in entries:
                if entry.name[::-1][:3][::-1]=="txt":
                    textFiles.append(entry.name)
        if len(textFiles)>=1:
            oW=rtry[1][ord(a[1])-32]
            final=""
            for q in range(0,len(textFiles)):
                print(str(q+1)+"-)",textFiles[q])
            line()
            fnm=input("File Name » ")
            line()
            f=open("operationFiles/"+textFiles[int(fnm)-1],"r")
            text=f.read().replace("\n","")
            f.close()
            for y in range(0,len(text)):
                oW=f_encrypt(oW,text[y],rtry)
                final=final+oW
            f = open("operationFiles/"+textFiles[int(fnm)-1][:len(textFiles[int(fnm)-1])-4]+".axen","a")
            f.write(final)
            f.close()
            print("Encryption process completed,",textFiles[int(fnm)-1][:len(textFiles[int(fnm)-1])-4]+".axen created.")
            line()
            pause()
        else:
            print("There is no file with .txt extension in the Keys & Texts file.")
            line()
            pause()
    elif int(obs)==1:
        oW=rtry[1][ord(a[1])-32]
        banner()
        line()
        final='"'
        text=input("Normal text » ")
        clear()
        banner()
        line()
        print('Normal text » "'+text+'"')
        line()
        for y in range(0,len(text)):
            oW=f_encrypt(oW,text[y],rtry)
            final=final+oW
        final=final+'"'
        print("Encrypted text »",final)
        line()
        pause()
    elif int(obs)==2:
        oW=rtry[1][ord(a[1])-32]
        banner()
        line()
        final=""
        text=input("Encrypted text » ")
        clear()
        banner()
        line()
        print('Encrypted text » "'+text+'"')
        line()
        for y in range(0,len(text)):
            nW=text[y]
            final=final+f_decrypt(oW,nW,rtry)
            oW=text[y]
        print('Decrypted text » "'+final+'"')
        line()
        pause()
    elif int(obs)==4:
        textFiles=[]
        textFiles.clear()
        with os.scandir('operationFiles/') as entries:
            for entry in entries:
                if entry.name[::-1][:4][::-1]=="axen":
                    textFiles.append(entry.name)
        banner()
        line()
        if len(textFiles)>=1:
            oW=rtry[1][ord(a[1])-32]
            for q in range(0,len(textFiles)):
                print(str(q+1)+"-)",textFiles[q])
            line()
            final=""
            fnm=input("Which file » ")
            line()
            f=open("operationFiles/"+textFiles[int(fnm)-1],"r")
            text=f.read().replace("\n","")
            f.close()
            for y in range(0,len(text)):
                nW=text[y]
                final=final+f_decrypt(oW,nW,rtry)
                oW=text[y]
            f = open("operationFiles/"+textFiles[int(fnm)-1][:len(textFiles[int(fnm)-1])-5]+".txt","a")
            f.write(final)
            f.close()
            print("Decryption process completed,",textFiles[int(fnm)-1][:len(textFiles[int(fnm)-1])-5]+".txt created.")
            line()
            pause()
        else:
            print("There is no file with .axen extension in the Keys & Texts file.")
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
