# The main purpose of any decorator is to change your class methods or attributes in such a way so that the user of your class no need to make any change in their code
# Getters and Setters in python are often used when:

# We use getters & setters to add validation logic around getting and setting a value.
# To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
# https://www.freecodecamp.org/news/python-property-decorator/

class Dog:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        print("Calling getter")
        return self.__name

    @property
    def age(self):
        print("Calling getter")
        return self.__age

    @age.setter
    def age(self, new_age):
        print("Calling setter")
        self.__age = new_age

    @name.setter
    def name(self, new_name):
        print("Calling setter")
        self.__name = new_name

    @name.deleter
    def name(self):
        print("Calling deleter")
        del self.__name


my_dog = Dog("Lucky", 33)

# name = my_dog.name
print(my_dog.name)
print("===")
my_dog.name = "Luckylo"
# my_dog.age = 88
print(my_dog.name)

del my_dog.name
