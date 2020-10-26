#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
def rnlm():
    rn=[]
    f=True
    while f==True:
        r=random.randint(1,40)
        if rn.count(r)==0:
            rn.append(r)
        if len(rn)==40:
            f=False
    return rn
rl=[[],[]]
rll=[[],[]]
for x in range(1,27):
    rl[0].append(chr(x+64))
ex_caracters=[" ",".",",",";",":","?","!","-","Ş","Ğ","Ü","Ö","Ç","İ"]
for z in range(0,len(ex_caracters)):
    rl[0].append(ex_caracters[z])

rl[1]=rnlm()
for y in range(1,41):
    for z in range(0,40):
        if y==rl[1][z]:
            rll[1].append(y)
            rll[0].append(rl[0][z])
rfn=random.randint(1,10**4)
fn="keys\\key"+str(rfn)+".ax"
f = open(fn, "a",encoding='utf-8')
for a in range(0,40):
    f.write(str(rll[1][a]))
    f.write("}")
    f.write(rll[0][a])
    if a==len(rl[0])-1:
        pass
    else:
        f.write("{")
f.close()
