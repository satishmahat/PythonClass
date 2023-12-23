# class Dog:
#     def __init__(self,breed):
#         self.var1=breed

# x=Dog(breed="German Shephard")

# print(x)
        
# print(x.var1)



class Cylinder:
    pi=3.14

    def calculateCSA(self,radius,height):
        self.csa=2*self.pi*radius*height
        print("The CSA of cylinder is: ",self.csa)

    def calculateTSA(self,radius,height):
        self.tsa= self.csa + 2*self.pi*radius**2
        print("The TSA of cylinder is: ",self.tsa)

a=Cylinder()
a.calculateCSA(7,3)
a.calculateTSA(7,3)
