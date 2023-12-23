

myList1=[2,3,4,5,6,7]
myList2=['a','e','i','o','u']
myzip=list(zip(myList1,myList2))   #the 6th element in myList1 doesnt have a pair
print(myzip)



#list comprehensions

# It allows us to build out list using different notaions
# You can think of it as essential a one line for loop inside of bracket
# grave every letter in a string

test=[x for x in "JAY-NEPAL"]
print(test)


# to print the square of a number in range list

y=list(range(0,11))
print(y)
z=[k*k for k in y]
print(z)


#
l=[m*m for m in range(0,23,3)]
print(l)



test1=[c for c in range(0,13) if c%2==0]
print(test1)

celcious=[0,40,100,-40,40]
fahrenheit=[((9/5)*temp+32) for temp in celcious]
print(fahrenheit)


#comprehension in nested list
result=[x**2 for x in [x**2 for x in range(0,12)]]
print(result)