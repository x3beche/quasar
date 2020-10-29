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

def keyComplier(fn):
    fn='key'+str(fn)+'.ax'
    f=open(fn,'r')
    klst=f.read().replace('\n','').split('split')
    f.close()
    a=klst[0].split('axen')
    rtry=[[],[]]
    for x in range(0,94):
        cache=klst[x].split('axen')
        rtry[0].append(cache[0])
        rtry[1].append(cache[1])
        cache.clear()
    return rtry,a

def axen(text,keyNumber):
    a=keyComplier(keyNumber)[1]
    rtry=keyComplier(keyNumber)[0]
    oW=rtry[1][ord(a[1])]
    final=''
    for y in range(0,len(text)):
        oW=f_encrypt(oW,text[y],rtry)
        final=final+oW
    return final
    
def axde(text,keyNumber):
    a=keyComplier(keyNumber)[1]
    rtry=keyComplier(keyNumber)[0]
    oW=rtry[1][ord(a[1])]
    final=''
    for y in range(0,len(text)):
        nW=text[y]
        final=final+f_decrypt(oW,nW,rtry)
        oW=text[y]
    return final
