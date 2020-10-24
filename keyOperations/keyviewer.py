import os
f=open("banner", "r")
print(f.read())
def opnr(data):
    f = open("key"+str(data), "r")
    klst=f.read().split(",")
    for x in range(0,len(klst)):
        print(klst[x])
data=input("Enter the number at the end of the key file : ")
os.system('cls' if os.name == 'nt' else 'clear')
opnr(data)
