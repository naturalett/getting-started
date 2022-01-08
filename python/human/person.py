import datetime

var = 5


class Person:
    def __init__(self, birth=None):
        self.name = "foo" or None
        self.age = 12 or None
        self.birth = birth
        self.id = 1234

    def get_age(self, today):
        return "99"
        # calculate = today - self.birth
        # return calculate


# Declaring my Object
# person = Person('2000-10-01')

#
# today = datetime.date.today()
# age = person.get_age(today)
# print((today))


# print(type(person.birth.split('-')[0]))

# print(type(datetime.date((person.birth))))
# print(f"Today is: {today}")
# age = person.get_age(today)
# print(person.id)


'''
p = Person()
dir(p)
p.name
p._age
p.__id
p._Person__id
'''
