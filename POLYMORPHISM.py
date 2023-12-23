# val1='hi'
# val2='k xa?'
# print(val1+'',val2)

# d1=4
# d2=7
# print(d1+d2)

# txt='welcome'
# print(len(txt))
# txt=['welcome','to', 'nepal']
# print(len(txt))


class Bird:
    def intro(self):
        print("Introduction")
    def fly(self):
        print("Flying")
class Pegion(Bird):
    def fly(self):      # method overriding (overloading not possible in python)
        print("Pegion can fly")
class Penguin(Bird):
    def fly(self):
        print("Penguin cant fly")


x=Bird()
x.intro()
x.fly()

y=Pegion()
y.intro()
y.fly()

z=Penguin()
z.intro()
z.fly()