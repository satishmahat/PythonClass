def squareFunction(a):
    return a%2==0
mylist=[2,3,4,5,6,7,8,9,10,12,13,14]

result=list(filter(squareFunction,mylist))
print(result)



def squareFunction(a):
    return a>3 and a<8
mylist=[2,3,4,5,6,7,8,9,10,12,13,14]

result=tuple(filter(squareFunction,mylist))
print(result)
