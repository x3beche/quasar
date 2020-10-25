f=open("banner", "r")
print(f.read())
f.close()
def opnr(data):
    print("\n")
    f = open("key"+str(data), "r")
    klst=f.read().split(",")
    for x in range(0,len(klst)):
        print(klst[x])
    f.close()
data=input("Enter the number at the end of the key file : ")
opnr(data)
