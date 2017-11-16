import random as r
def seed(x,y=0):
    r.seed(x)
    r.jumpahead(y)

def genIco(r, random):
    x = []
    for j in range(12):
        x.append(r+r.randint(0-random,random))
    return x

 def newVerts(q):
     y = 30
     for j in range(q-1):
         y = y*4
     return y

def vertHeight(ico, n, q):
    #code should be here

def subIco(ico, q, random):
    x = ico
    for j in range(newVerts(q)):
        #needs to average height of surrounding nodes first
        #each vert only has 2 "parents"
        #function to determine parents, then average their heights.
        x.append(vertHeight(ico, j, q)+r.randint(0-random,random))
    return x

seed(1)
change = 1024
icosphere = genIco(13000, change)
for j in range(5):
    change = change/2
    icoshpere = subIco(icosphere, j+1, change)
