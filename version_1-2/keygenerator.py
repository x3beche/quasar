import random
def rnlm():
    rn=[]
    f=True
    while f==True:
        r=random.randint(1,34)
        if rn.count(r)==0:
            rn.append(r)
        if len(rn)==34:
            f=False
    return rn
rl=[[],[]]
rll=[[],[]]
for x in range(1,27):
    rl[0].append(chr(x+64))
rl[0].append(" ")
rl[0].append(".")
rl[0].append(",")
rl[0].append(";")
rl[0].append(":")
rl[0].append("?")
rl[0].append("!")
rl[0].append("-")
rl[1]=rnlm()
for y in range(1,35):
    for z in range(0,34):
        if y==rl[1][z]:
            rll[1].append(y)
            rll[0].append(rl[0][z])
rfn=random.randint(1,10**4)
fn="key"+str(rfn)+".ax"
f = open(fn, "a")
for a in range(0,34):
    f.write(str(rll[1][a]))
    f.write("}")
    f.write(rll[0][a])
    if a==len(rl[0])-1:
        pass
    else:
        f.write("{")
f.close()
