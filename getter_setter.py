class BankUSD:
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return f'Bank ILS {self.balance}'
    @property
    def balance(self):
        return self.__balance * 3.5
    @balance.setter
    def balance(self, value):
        self.__balance = value / 3.5


u = BankUSD(43500)
print(u)
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = None
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value

    def __str__(self):
        return f'Person {self.name} {self.__age}'

p = Person('Moshe', -5)
print(p.age) # get
p.age = -3 # set
p.age = 31 # set
print(p)


    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value >= 0:
            self.__age = value

'''

# Create class computer
# property model
# setter will not allow model with name smaller than 4 characters


