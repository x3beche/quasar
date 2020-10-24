f=open("keyOperations\\banner", "r")
print(f.read())
f.close()

fn="keyOperations\\key1001"
f=open(fn,"r")
klst=f.read().split(",")
rtry=[[],[]]
for x in range(0,26):
    cache=klst[x].split("-")
    rtry[0].append(cache[0])
    rtry[1].append(cache[1])
    exec(rtry[1][x]+"=rtry[0][x]")
    cache.clear()

print(A,B,C,D,E,F,G)
