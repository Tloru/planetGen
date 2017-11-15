# planetGen
planetGen genetrates realistic rocky planets through subdividing icospheres. How does it work exaclty?
# Functionality
the idea is simple - starting out with a 12-vertex icoshpere, apply random noise to each of the verticies. Based on the height of the surrounding vertices calculate the height of the new one, then apply random noise yet again (with less altitude variation). With a specific seed, you will always get the same planet - and each planet in infinetly refinable. 
# Pseudocode
This is just to get my thoughts in place.

seed = 1 <br>
genIco(size) <br>
change = 1024 <br>
repeat 5 <br>
  randIco(change) <br>
  change = change/2 <br>
