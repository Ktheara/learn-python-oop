#https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/
#video: 57:50

class car:
    def __init__(self, name, price):
        self.__name = name          # Attritbute is protected, only method in class a acceable.
        self.price = price

    def Name(self):
        return f"This is {self.__name}."  # Access protected attribute by method in class.

    def setPrice(self, price):
        self.price = price
    
    def _calcPrice(self):           # internal method
        return self.price*2

    def sellPrice(self):
        print(f"This price of this {self.__name} is {self._calcPrice()} dollar")
    
mycar1 = car("Toyota", 30000)
print(mycar1.Name())

#print(mycar1.__name)                # This will error try to access attribute by outside class.

mycar1.setPrice(59000)
mycar1.sellPrice()