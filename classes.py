# def add(x, y):
#     return x + y

# sum = add(4, 5)
# print(sum)

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("Eating...")
    def breathe(self):
        print("Breathhing...")

# animal1 = Animal("dog")
# animal1.eat()

class Dog(Animal):
    def sound(self):
        print("Breaking...")

class Cat(Animal):
    def sound(self):
        print("Meow...")

dog1 = Dog("Hatchi")
dog1.eat()
dog1.sound()

cat1 = Cat("cat")
cat1.eat()
cat1.sound()