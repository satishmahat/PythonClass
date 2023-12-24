# a=20
# b=0

# print("Division : ",a/b)

# print("hi"+5)
# try:
#     print(x)
# except NameError:
#     print("cannot be defined")
# except:
#     print("Cannot defined by zero")




# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")




# try:
#   f = open("one.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     # print("xyz")
#     f.close()
# except:
#   print("Something went wrong when opening the file")


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
