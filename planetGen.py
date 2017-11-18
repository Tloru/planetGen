import random as ra

#planetGen


def seed(x,y=0):
    ra.seed(x)
    ra.jumpahead(y)

#tri1
#    1x
#   /  \
#  /    \
# /      \
#2y ____ 3z

#tri2
#2y ---- 3z
# \      /
#  \    /
#   \  /
#    x

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def genIcoTri(x, r, random):
    #each triangle covers around 40 million square kilometers.
    global alphabet
    tri = []
    if x == 0: #a block ---------- g
        for j in range(3):
            tri.append(r+(ra.uniform(0-random,random)))
    if x >= 1 and x <= 3: #bcd
        tri.append("a[1]")
        tri.append(str(alphabet[x-1])+"[3]")
        tri.append(r+(ra.uniform(0-random,random)))
    if x == 4: #e
        tri.append("a[1]")
        tri.append("d[3]")
        tri.append("a[2]")
    if x == 5: #f block ---------- g
        tri.append(r+(ra.uniform(0-random,random)))
        tri.append("a[2]")
        tri.append("a[3]")
    if x >= 6 and x <= 8: #ghi
        tri.append(r+(ra.uniform(0-random,random)))
        tri.append(str(alphabet[x-6])+"[3]")
        tri.append(str(alphabet[x-5])+"[3]")
    if x == 9: #j
        tri.append(r+(ra.uniform(0-random,random)))
        tri.append("d[3]")
        tri.append("a[2]")
    if x == 10: #k block ---------- g
        tri.append("a[3]")
        tri.append("f[1]")
        tri.append("g[1]")
    if x >= 11 and x <= 13: #lmn
        tri.append(str(alphabet[x-10])+"[3]")
        tri.append(str(alphabet[x-5])+"[1]")
        tri.append(str(alphabet[x-4])+"[1]")
    if x == 14: #o
        tri.append("a[2]")
        tri.append("j[1]")
        tri.append("f[1]")
    if x == 15: #p block ---------- g
        tri.append(r+(ra.uniform(0-random,random)))
        tri.append("f[1]")
        tri.append("g[1]")
    if x >= 16 and x <= 18: #qrs
        tri.append("p[1]")
        tri.append(str(alphabet[x-10])+"[1]")
        tri.append(str(alphabet[x-9])+"[1]")
    if x == 19:
        tri.append("p[1]")
        tri.append("j[1]")
        tri.append("f[1]")
    return tri

def genPlanet(r, random):
    dic = {}
    for j in range(20):
        dic[str(alphabet[j])] = genIcoTri(j, r, random)
        dic['quality'] = 1
    return dic

def getTri(dic, t):
    z = dic
    w = []
    for j in range(3):
        x = t[j]
        if isinstance (x, str):
            y = x[0]
            y = z[str(y)]
            x = y[int(x[2])-1]
        w.append(x)
    print w
    return w

def subTri(dic, quality):
    for j in range(20):
        x = getTri(dic, dic[str(alphabet[j])])


change = 20.48
planet = genPlanet(1000, 0)
print planet

print
print "sample planet generation at quality one (1) complete"
print
#planet = subTri(planet)
