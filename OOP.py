#OOP -> Object oriented programming

#we determine the type of object using type() method

print(type(7))
print(type((1,2,3,4,5,6)))

#to create an objects we use 'class' keyword
#class: user defined objects are created using keyword 'class'
#The class is a blueprint that defines the nature of future objects
#from classes we can construct instances
#An instance is specific object created from particular class
# for example above we create the object list which has instanc of list object

#create a new object type called demo

class demo:
    pass
x=demo() 
print(type(x))

