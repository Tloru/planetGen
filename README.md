# planetGen
planetGen originally genetrated realistic rocky planets through subdividing icospheres. Due to complications, as well as optimizing for faster render times, we're now using cubes. How does it work?
# Functionality
the idea is simple - starting out with a 8-vertex cube, apply random noise to each of the verticies. Take each of the faces (which are now squares) and apply a set amount of random noise to them. You can then divide each of the faces in to fourths and repeat this process. With a specific seed, you will always get the same planet - and each planet in infinetly refinable. 
# To-Do
Right now, planetGenerates a whole planet at a time. I think it would work a lot better if it generated only the area you could see. 
