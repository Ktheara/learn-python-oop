#Learn class
#https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/

en1 = ["Devid", 32, 783]
en1 = ["Janny", 25, 583]

class Engineer:
    #class attributes | same to all object
    level = "S1"
    def __init__(self, name, age, salary):
        #instance attributes | only belong to one object
        self.name = name
        self.age = age
        self.salary = salary
    #instance method
    def code(self):
        print(f"{self.name} is writing code.")
    def code_language(self, language):
        print(f"{self.name} is writing code in {language}")
    def info(self):
        info = f"name = {self.name}, age = {self.age}, salary = {self.salary}"
        return info
    def __eq__(self, other): #check if object element are equal
        return self.age == other.age

#instance
Eng1 = Engineer("Mac", 23, 730)
Eng2 = Engineer("Janny", 23, 586)
Eng1.code()
Eng1.code_language("python")
print(Eng1.info())
print(Eng1 == Eng2)
#end of oop2