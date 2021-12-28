from person import Person

class Employee(Person):
    def __init__(self):
        Person.__init__(self)        
        self.__id = 25


'''
emp = Employee()
dir(emp)
emp.__id
emp._Person__id
emp._Employee__id
'''