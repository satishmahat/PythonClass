class Animal:
    def __init__(self):
        print("ANIMAL CLASS CREATED")
    def WhoIs(self):
        print("Animal")
    def eat(self):
        print("Animal who eat.")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)

        # print("DOG CLASS CREATED")
        pass
    def WhoIs(self):
        print("Type of animal")
    def speak(self):
        print("Dog is barking")


# a=Animal()
# print(a)
# a.WhoIs()
# a.eat()

# a.speak()

b=Dog()
b.WhoIs()
b.eat()
b.speak()

