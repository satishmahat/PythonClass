from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius**2
    
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    
areacircle=Circle(4)
print("The area of Circle : ", areacircle.area())

arearect=Rectangle(10,20)
print("The area of Recatangle : ", arearect.area())



# class sushant(ABC):
#     @abstractmethod
#     def __init__ (self,name,height):
#         self.name=name
#         self.height=height

#     def buero(self):
#         print('k xa?')
    
# kunwar=sushant('aasu',5.3)
# kunwar.buero()
# print(kunwar.height)
