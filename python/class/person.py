class Person:
    def __init__(self):
        self.name = 'Sarah'
        self._age = 26
        self.__id = 30


'''
p = Person()
dir(p)
p.name
p._age
p.__id
p._Person__id
'''