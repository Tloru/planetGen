#tested seeding - works fine.
import random as ra
import numpy as np

startseed = 20040319
ra.seed(startseed)

planet = 251

#planets = 100000000000*ra.uniform(1,9)

ra.jumpahead(planet)

#size in km (diameter)
planetsize = ra.uniform(1000,15000)

x=2
print(12+(30*4*x))

print(planetsize)

def icoverts(quality):
    x = 12
    y = 30
    for j in range(quality-1):
        x += y
        y = y*4
    return x

def surfacenoise(quality):
    global planetsize
    x = 21000/13000*planetsize
    for j in range(quality):
        x = x/2
    return x*2
    #-10,000 to 10,0000 mountain ranges
    #21,000 to -21,000 bulger


def planetsurface(quality):
    surface = [1]
    x = 12
    y = 30
    for j in range(quality-1):
        for a in range(j):
            surface.append(uniform(surfacenoise(a+1),(0-surfacenoise(a+1))))
        x += y
        y = y*4
    return surface



#12, 42, 162, 642, 2562
#30, 120, 480, 1920

print(icoverts(3))
print(planetsurface(1))

print
print("testing complete")
print

#-----
#functions
#-----

def seed(x,y=0):
    ra.seed(x)
    ra.jumpahead(y)

def genIco(r, random):
    x = []
    for j in range(12):
        x.append(r+(ra.uniform(0-random,random)/1000))

    return x

def newVerts(q):
     y = 30
     for j in range(q-1):
         y = y*4
     return y

def vertHeight(ico, n, q):
    #code should be here
    return 0

def subIco(ico, q, random):
    x = ico
    for j in range(newVerts(q)):
        #needs to average height of surrounding nodes first
        #each vert only has 2 "parents"
        #function to determine parents, then average their heights.
        x.append(vertHeight(ico, j, q)+(ra.uniform(0-(random),(random))/1000))
    return x

seed(1)
change = 21000
icosphere = genIco(13000, change)
for j in range(5):
    change = change/2
    icoshpere = subIco(icosphere, j+1, change)
print icosphere

print
print "ico build complete"
print "moving to triangle seeding"
print

def seed(x,y=0):
    ra.seed(x)
    ra.jumpahead(y)

#     1
#   /  \
#  /    \
# /      \
#2 ______ 3

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def genIcoTri(x, r, random):
    global alphabet
    tri = []
    if x == 0:
        for j in range(3):
            tri.append(r+(ra.uniform(0-random,random)))
    if x >= 1 and x <= 3:
        tri.append("a1")
        tri.append(str(alphabet[x-1])+"3")
        tri.append(r+(ra.uniform(0-random,random)))
    if x == 4:
        tri.append("a1")
        tri.append("d2")
        tri.append("a2")
    if x >= 5 and x <= 15:
        #tri.append()
    return tri

for j in range(20):
    print(genIcoTri(j, 5, 1))