class Animal(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Animal {self.name}'

class Bird(Animal):
    def __init__(self, name,
                 flySpeed):
        #self.name = name
        #super().__init__(name)
        #Animal.__init__(self, name)
        super().__init__(name)
        self.flySpeed = flySpeed
    def __str__(self):
        return f'{super().__str__()}'\
    f' {self.flySpeed}'
    def __gt__(self, other):
        if (isinstance(other, Bird)):
            if self.flySpeed > other.flySpeed:
                return True
            else:
                return False

cat = Animal('Tom')
print(cat)
twitty = Bird('Twitty', 515)
jet = Bird('Jet', 718)

print(twitty)
print(twitty > jet)
print(twitty > 'hello')
print(isinstance(twitty, Animal))
print(issubclass(Bird, Animal))
print(issubclass(Animal, Animal))

# create Person class with name, age
# create subclass of Employee
# which inherits from Person
# and also have salary
# create Manager class inherites
# from Employee and has number
# of employees he manages
# write init which calls super
# write __str__ which calls super







