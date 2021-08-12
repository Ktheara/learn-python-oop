# Ingeritance is one class inherits the attributes and methods of another.

class Employee:                     #parent class
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    
    def work(self):
        return f"{self.name} is working."

class SoftwareEngineer(Employee):   #child class
    def __init__(self, name, age, level, salary):
        super().__init__(name, age) #initialize parent class using "supper"
        self.level = level
        self.salary = salary

    def debugging(self):            #method only belong to SoftwareEngineer
        return f"{self.name} is debugging."

    def work(self):                 #override method "work" of parent class
        return f"{self.name} is coding."

class Designer(Employee):           #child class
    def drawing(self):
        return f"{self.name} is drawing."
    
    def work(self):                 #override method "work" of parent class
        return f"{self.name} is designing."

em1 = Employee("Jan", 34)
d1 = Designer("Gem", 23)
sof1 = SoftwareEngineer("Tom", 40, "Senior", 900)

print(em1.name, em1.age)
print(d1.name, d1.age, d1.work())
print(d1.work())
print(sof1.name, sof1.age, sof1.age, sof1.level, sof1.salary)
print(sof1.work())
print(sof1.debugging())