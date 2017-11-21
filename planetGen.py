#-----
#planetGen
#-----

import random as ra #importing random module

ra.seed(20040319) #sets the seed of the planet
pSize = 6000000 #planet size slightly smaller than earth's (radius)
pArea =  4*3.14*(pSize/1000)**2 #surface area of planet in km^2

def calcQuality(sA, qS): #calculates the quality level needed to achieve a certain distance between nodes
    j = -1 #j is the amount of quality needed
    x = sA/6 #divided the total surface area by 6, the size of each face on the cube
    while True: #repeat until loop
        j+=1 #counter goes up
        print str(x)+" "+str(j) #displays the current tile size and quality
        if x <= qS: #breaks loop when conditions are met
            return j-1 #returns the counter
        else: #else
            x = int(x/4) #divides the surface further into 4 more pieces

quality = calcQuality(pArea, 1000) #sets the quality of the planet
print(pArea)
print(quality)

pVari = 21000 #planet variation (ie. maximum mountain height) | all units are in meters
a = ["1", pSize + ra.randint(0 - pVari, pVari)] #top
b = ["1", pSize + ra.randint(0 - pVari, pVari)] #front
c = ["1", pSize + ra.randint(0 - pVari, pVari)] #left
d = ["1", pSize + ra.randint(0 - pVari, pVari)] #back
e = ["1", pSize + ra.randint(0 - pVari, pVari)] #right
f = ["1", pSize + ra.randint(0 - pVari, pVari)] #bottom

def divide(li, section = "None"): #this function divides a face of the planet into a smaller portion
    nLi = [] #stands for "new list"
    if section == "None": #divides one part of the world by one step, no matter the quality before
        for j in range(len(li)): #repeats for each value in the list
            x = li[j] #takes an individual value from the list
            if str(type(x)) == "<type 'str'>":
                y = str(1+int(x))
            else:
                for j in range(4): #divides the list into 4 equal parts
                    nLi.append(y)
                    nLi.append(x + ra.randint(0 - pVari, pVari)) #adds value to nLi with some randomness
    else:
        nli = []
    return nLi #returns the subdivided list

for j in range(quality): #repeats the amout nescary for each value to represent roughly a meter of space (15 times)
    pVari = pVari / 3 #makes things less random as they get smaller
    a = divide(a) #divides the top
    b = divide(b) #divides the front
    c = divide(c) #divides the left
    d = divide(d) #divides the back
    e = divide(e) #divides the right
    f = divide(f) #divides the bottom
    print j #displays what division step it's currently on

print a #displays the top surface values
print b # ^ front
print c # ^ left
print d # ^ back
print e # ^ right
print f # ^ bottom
