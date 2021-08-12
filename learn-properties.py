# A decorator feature in Python wraps in a function, appends several functionalities to existing code and then returns it.
# https://www.geeksforgeeks.org/python-property-decorator-property/

class Portal:
    def __init__(self):
        self.__name = ''
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        self.__name = val

    @name.deleter
    def name(self):
        del self.__name


#create attribute
p = Portal()

#set name
p.name = 'Theara'

#get name
print(p.name)

#delete name
del p.name

#try to get name, error because there's no longger has a name value
print(p.name)
