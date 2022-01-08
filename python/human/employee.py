from person import Person

class Employee(Person):
    def __init__(self):
        Person.__init__(self)        
        self.id = 25

    def get_age(self):
        pass




person = Person("2000-12-01")
emp = Employee(Person)
print(emp.age)
























'''
emp = Employee()
dir(emp)
emp.__id
emp._Person__id
emp._Employee__id
'''