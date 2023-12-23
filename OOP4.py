class circle:
    pi=3.14

    #circle gets instantiated with a radius 

    def __init__(self,radius=5):
        self.leng=radius
        self.area=self.pi*radius**2

    def setRadius(self,newRadius):
        self.radius1=newRadius
        self.area1=self.pi*newRadius**2

    def circle2(self,radius2):
        self.radius2=radius2
        self.circum=2*circle.pi*radius2

a=circle()
print('\nRadius : ',a.leng)
print('Area : ',a.area)

a.setRadius(7)
print('\nNew Radius : ',a.radius1)
print('New Area : ',a.area1)

a.circle2(5)
print('\nNew circle radius : ',a.radius2)
print('Circumference : ',a.circum )




