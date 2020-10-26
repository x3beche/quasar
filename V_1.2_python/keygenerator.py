#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random,time
def line():
    print("-----------------------------------------------------")
def banner():
    f=open("easy_command\\banner", "r")
    print(f.read())
    f.close()
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
ex_caracters=[" ",".",",",";",":","?","!","-"]
for z in range(0,len(ex_caracters)):
    rl[0].append(ex_caracters[z])

rl[1]=rnlm()
for y in range(1,35):
    for z in range(0,34):
        if y==rl[1][z]:
            rll[1].append(y)
            rll[0].append(rl[0][z])
rfn=random.randint(1,10**4)
fn="operationFiles\\key"+str(rfn)+".ax"
f = open(fn, "a",encoding='utf-8')
for a in range(0,34):
    f.write(str(rll[1][a]))
    f.write("}")
    f.write(rll[0][a])
    if a==len(rl[0])-1:
        pass
    else:
        f.write("{")
f.close()

banner()
line()
print("Random password file generated and saved : key"+str(rfn)+".ax")
line()
time.sleep(5)
