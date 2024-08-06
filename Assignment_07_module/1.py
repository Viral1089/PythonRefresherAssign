class Animal():
    #initialization of variables (constructor)
    def __init__(self,name,species,weight):
        self.name = name
        self.species = species
        self.weight = weight
    #it is a function which gives the information about there name ,Species and weight.
    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Weight: {self.weight} kg")
        
#creating a subclass cow which uses base class (Animal) methods called inheritance.
class Cow(Animal):
    def eat(self):
        print("I does eat Green Grass.")
    def speak(self):
        print("I used to speak \'Moo\'.")
        print()
        

class Horse(Animal):
    def eat(self):
        print("I am eating Green Grass and Hay.")
    def speak(self):
        print("I used to speak \'Neigh\'.")
        print()
        
class Dog(Animal):
    def eat(self):
        print("I am eating Bean and Biscuits.")
    def speak(self):
        print("I used to speak \'Woof\'.")
        print()
        
#creating instance of Cow subclass     
c = Cow("Kalawati","Jersy",200)
c.info()                #method from base class
c.eat()
c.speak()

#creating instance of Horse subclass
h = Horse("Chetak","Arabian",250)
h.info()                #method from base class
h.eat()
h.speak()

#creating instance of Dog subclass
d = Dog("Puppy","German Shepherd",30)
d.info()                #method from base class
d.eat()
d.speak()
