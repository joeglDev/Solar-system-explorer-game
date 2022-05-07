#USE CASES

#1. Procedural object genration of planets (attributes), moons (attributes), solar systems 
#create object contructor, give it a list of possible inputs, randomise selection
#2. Storage of these generated objects for later
#3. Ability for user to visit diff objects in a text based game
#4. stretch - format text into a nice GUI

#1 World Generation

from random import choice, randint


#distance from star in AU, radius in km

#generate random vars

#note currently classes are nonsensical so write if else statement to give numbers based on planet class
class Planet:
    """
    Constructor to create planet object.
    """
    def __init__(self, name, stellarDistance, radius, composition, worldType, moons):
        self.name = name
        self.stellarDistance = stellarDistance
        self.radius = radius
        self.composition = composition
        self.worldType = worldType
        self.moons = moons

    def printVars(self):
        print(f"{self.__class__.__name__}: {self.name}")
        for var in self.__dict__.items(): 
            print(var)
    


    
        
#Baked in Planets
Earth = Planet("Earth", 1 , 6371, "Rocky", "Continental", 1)
#Earth.printVars()
Tal = Planet("Tal", 1, 7000, "Rocky", "Savanna", 0)
#Tal.printVars()


def newPlanet():
    """
    Generates a random instamce of planet.
    """
    name = ["Hex", "Whisp", "Lucifer", "Ix", "Mary's Planet", "Gaia", "Evie-Prime"]
    stellarDistance = randint(0, 40)
    radius = randint(1000, 70000)
    composition = ["Arid", "Desert", "Savanna", "Alpine", "Arctic", "Tundra", "Tropical", "Continental", "Ocean"]
    worldType = ["Dwarf", "Earth", "Super-Earth", "Gas Giant", "Ring World"]
    moons = randint(0, 5)
    
    newPlanet = Planet(choice(name), stellarDistance, radius, choice(composition), choice(worldType), moons)
    newPlanet.printVars()
    
newPlanet() 







#Planets

#Moons

#Other Objects-belts, rogues, exotic objects, 

#Solar System (call other functions)

