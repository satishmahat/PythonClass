
#defining the function 
# def demoFunction():
#     print("This is a user defined function \n" )   
    # pass -> is used in empty function to minimize error
#call the function
# demoFunction()


#function with argument

# def testFunction(first_value,second_value):
#     print('First Value=',first_value,'Second Value=',second_value)

# testFunction(23,45)


#return type

# def multiply(a,b):
#     return a*b


# result=multiply(5,4)
# print(result)



#suffle

from random import shuffle
# mylist=[1,2,3,4,5]
# shuffle(mylist)
# print(mylist)


# Interaaction with different function

# def shuffle1(a):
#     shuffle(a)
#     return a
# mylist2=['A','P','P','L','E']
# result=shuffle1(mylist2)
# print(result)

#returning tuples for unpacking
#recall we can loop through a list of tuples and unpack values within them

# free_transfer=[('MESSI',700),('BENZEMA',150),('SILVA',75),('POCCHETINO',85)]

# for player in free_transfer:
#     print(player)

# for player,market_value in free_transfer:
#     print(player)
# for player,market_value in free_transfer:
#     print(market_value)




#code1


# def add(a,b):
#     return(a+b)
# def sub(a,b):
#     return(a-b)
# def mult(a,b):
#     return(a*b)

# value1= int(input("Enter first number: "))
# value2= int(input("Enter second number: "))

# a=add(value1,value2)
# s=sub(value1,value2)
# m=mult(value1,value2)


# print("SUM=",a)
# print("DIFF=",s)
# print("MULT=",m)



#code2

# def messi(a,b):    #see file day5
#     print(a+b)


def sq(a):
    print("Square of ",a,"is",a**2)

list=[1,2,3,4,5]

for list in list:
    sq(list)









    