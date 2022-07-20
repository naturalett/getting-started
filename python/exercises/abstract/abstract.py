# Data Abstraction firstly saves a lot of our time as we do not have to repeat the code that may be the same for all the classes. Moreover, if there are any additional features, they can be easily added, thus improving flexibility. Not to mention, working in large teams becomes easier as one won’t have to remember every function and the basic structure can be inherited without any confusions.

from abc import ABC,abstractmethod
 
class Animal(ABC):
 
    #concrete method
    def sleep(self):
        print("I am going to sleep in a while")
 
    @abstractmethod
    def sound(self):
        print("This function is for defining the sound by any animal")
        pass
 
class Snake(Animal):
    def sound(self):
        print("I can hiss")
 
class Dog(Animal):
    def sound(self):
        print("I can bark")
 
class Lion(Animal):
    def sound(self):
        print("I can roar")
       
class Cat(Animal):
    def sound(self):
        print("I can meow")

# Now, if we want to access the sound() function of the base class itself, we can use the object of the child class, but we will have to invoke it through super()

class Rabbit(Animal):
    def sound(self):
        super().sound()
        print("I can squeak")

c = Cat()
c.sleep()
c.sound()
 
c = Snake()
c.sound()

r = Rabbit()
r.sound()