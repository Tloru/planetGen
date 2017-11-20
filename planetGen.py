#-----
#planetGen
#-----

import random as ra #importing random module

pSize = 13000000 #planet size slightly larger than earth's
pVari = 21000 #planet variation
a = [pSize + ra.uniform(0 - pVari, pVari)] #top
b = [pSize + ra.uniform(0 - pVari, pVari)] #front
c = [pSize + ra.uniform(0 - pVari, pVari)] #left
d = [pSize + ra.uniform(0 - pVari, pVari)] #back
e = [pSize + ra.uniform(0 - pVari, pVari)] #right
f = [pSize + ra.uniform(0 - pVari, pVari)] #bottom

def divide(li): #this function divides a face of the planet into a smaller portion
    nLi = [] #stands for "new list"
    for j in range(len(li)): #repeats for each value in the list
        x = li[j] #takes an individual value from the list
        for j in range(4): #divides the list into 4 equal parts
            nLi.append(x + ra.uniform(0 - pVari, pVari)) #adds value to nLi with some randomness
    return nLi #returns the subdivided list

for j in range(26): #repeats the amout nescary for each value to represent roughly a meter of space (26 times)
    pVari = pVari / 2 #makes things less random as they get smaller
    a = divide(a) #divides the top
    b = divide(b) #divides the front
    c = divide(c) #divides the left
    d = divide(d) #divides the back
    e = divide(e) #divides the right
    f = divide(f) #divides the bottom

print a #displays the top surface values
print b # ^ front
print c # ^ left
print d # ^ back
print e # ^ right
print f # ^ bottom
