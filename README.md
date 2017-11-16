# planetGen
planetGen genetrates realistic rocky planets through subdividing icospheres. How does it work?
# Functionality
the idea is simple - starting out with a 12-vertex icoshpere, apply random noise to each of the verticies. Based on the height of the surrounding vertices calculate the height of the new one, then apply random noise yet again (with less altitude variation). With a specific seed, you will always get the same planet - and each planet in infinetly refinable. 
# Pseudocode
This is just to get my thoughts in place.

seed = 1 #seed can be anything - here I set it to 1 <br>
genIco(size) #generates an icosphere with a radius of size <br>
change = 1024 #maximum and minimum deviaion of each vertex for randIco() <br>
repeat(5){ #loop :D (5 is quality, btw) <br> 
subIco() #subdivides the ico, and averages out new vertices  <br>
randIco(change) #randomizes new vertices with change<br>
change = change/2 #decreases change<br>
}
