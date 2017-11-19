# planetGen
planetGen originally genetrated realistic rocky planets through subdividing icospheres. Due to complications, as well as optimizing for faster render times, we're now using cubes. How does it work?
# Functionality
the idea is simple - starting out with a 8-vertex cube, apply random noise to each of the verticies. Take each of the faces (which are now squares) and apply a set amount of random noise to them. You can then divide each of the squares in to fourths and repeat this process. With a specific seed, you will always get the same planet - and each planet in infinetly refinable. 
# Pseudocode
This is just to get my thoughts in place.

seed = 1 #seed can be anything - here I set it to 1 <br>
genCube(size) #generates a cube with a radius of size <br>
change = 1024 #maximum and minimum deviaion of each vertex for randCube() <br>
repeat(5){ #loop :D (5 is quality, btw) <br> 
subCube() #subdivides the cube, and averages out new vertices  <br>
randIco(change) #randomizes new vertices with change<br>
change = change/2 #decreases change<br>
}
