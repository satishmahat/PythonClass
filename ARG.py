# *arg -> when a function parameter starts  with asterisk , it allows an arbitary number of arguments and the function takes them in as a tuple of the value


# def myfunction(*a):
#     return a*2

# test=myfunction(10,20,30,40)
# print(test)


#string

# def myfunction(*args):
#     return len(args)

# test=myfunction('hi','namaste')
# print(test)


# **kwargs -> it handles arbitary number of keyworded argument
# insted of creatig a tuple of values **kwags build dictionary of key/value pairs

# def demoFunc(**kwargs):
#     if 'fruit' in kwargs:
#         return print(f"My favourite fruit is {kwargs['fruit']}")
#     else:
#         return 0
    
# result=demoFunc(fruit='orange')
# print(result)


# *args and **kwargs combination

def mychoice(*args,**kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favourite fruit is {kwargs['fruit']}")
        print(f"May i have {kwargs['juice']} juice please?")

    else:
        pass

mychoice("eggs","fish",fruit="garpes",juice="mango")
