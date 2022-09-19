# - your class has a working constructor method (__init__).
# - your class has at least 4 values (instance variables).
# - your class has at least 2 actions (methods.functions) in addition to the constructor method.
# - your module also contains a working main mthod.
# - your main method creates at least 2 instances of your animal class.
# - your main method prints out at least 2 values for the instances to show how theya re different.
# - your main method changes at least 1 value of an instance and then prints it out to show it has changed.

class Animal:
    def __init__(self, clas, genus, species, colour):
        self.clas = clas
        
        self.genus = genus
        
        self.species = species
        
        self.colour = colour

    def getClas(self):
            return self.clas
        
    def getGenus(self):
            return self.genus
        
    def getSpecies(self):
            return self.species
        
    def getColour(self):
            return self.colour
        

    def setColour(self, grey):
        self.colour = grey
        
    
def main():
    anim1 = Animal("Lizard", "Uromastyx", "Ornata", "Sky Blue")
    anim2 = Animal("Lizard", "Uromastyx", "Benti", "Tan")

    print(anim1.getClas())
    print(anim1.getGenus())
    print(anim2.getColour())
    anim2.setColour("Grey")
    print(anim2.getColour())

if __name__ == "__main__":
    main()
