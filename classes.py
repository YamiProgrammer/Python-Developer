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

animal1 = Animal("dog")
animal1.eat()