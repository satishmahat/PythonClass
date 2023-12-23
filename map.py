def squareFunction(a):
    return a**2
mylist=[2,3,4,5,6]

result=list(map(squareFunction,mylist))
print(result)



def checkFunction(b):
    if len(b)%2==0:
        return "EVEN"
    else:
        return b
    
player=['messi','neymar','ronaldo','ibrahmovic']
results=list(map(checkFunction,player))
print(results)