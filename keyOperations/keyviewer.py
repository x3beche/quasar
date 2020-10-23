while True:
    data=input("Enter the number at the end of the key file : ")

    f = open("key"+str(data), "r")
    klst=f.read().split(",")

    for x in range(0,len(klst)):
        print(klst[x])
