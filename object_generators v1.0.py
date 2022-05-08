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
    def __init__(self, name, stellarDistance, radius, climate, worldType, moons):
        self.name = name
        self.stellarDistance = stellarDistance
        self.radius = radius
        self.climate = climate
        self.worldType = worldType
        self.moons = moons

    def printVars(self):
        print(f"{self.__class__.__name__}: {self.name}")
        for var in self.__dict__.items(): 
            print(var)

  

#Tal.printVars()
#Earth.printVars()

#planet variable lists
planets = []
#Baked in Planets
Earth = Planet("Earth", 1 , 6371, "Continental", "Earth-Like",  1)
Tal = Planet("Tal", 1, 7000,"Savanna", "Earth-Like",  0)
planets.append(Earth)
planets.append(Tal)

name = ["Hex", "Whisp", "Lucifer", "Ix", "Mary's Planet", "Gaia", "Evie-Prime"]
radius = randint(1000, 70000)
climate = ["Arid", "Desert", "Savanna", "Alpine", "Arctic", "Tundra", "Tropical", "Continental", "Ocean"]
gasGiantClimate = ["Ammonia clouds", "Water clouds", "Cloudless", "Alkali-metal clouds", "Silicate clouds"]
worldType = ["Dwarf", "Earth-like", "Super-Earth", "Gas Giant"]


def makePlanet(numOf):
    """
    Generates defined number of instances of Planet objects. 
    """
    count = 0
    while count < numOf:
        #make Planet
        newPlanet = Planet(
        name = choice(name),
        stellarDistance = randint(0, 40),
        worldType = choice(worldType),
        radius = "TBC",
        climate = choice(climate),
        moons = randint(0,5))

        #adjust variables of planet for realism
        if newPlanet.worldType == "Dwarf":
             newPlanet.radius = randint(838, 2000)
             newPlanet.climate = "Barren"
        elif newPlanet.worldType == "Earth-like":
             newPlanet.radius = randint(5096, 7645)
             newPlanet.stellarDistance = randint(8, 12) / 10
        elif newPlanet.worldType == "Super-Earth":
             newPlanet.radius = randint(7646, 12742)
        elif newPlanet.worldType == "Gas Giant":
             newPlanet.radius = randint(20000, 80000)
             newPlanet.climate = "Surfaceless"
         
        #append Planets to a global list
        planets.append(newPlanet)
        count = count + 1
    
makePlanet(5)
for i in range(5+2):
    print(vars(planets[i]))








#Planets

#Moons

#Other Objects-belts, rogues, exotic objects, 

#Solar System (call other functions)

