
#iteration over elements in a list

# fruits=["apple","banana","cherry"]
# for fruit in fruits:
#     print(fruit)

#iteration over a range of numbers

# for i in range(1,5):
#     print(i)

#iterate over characters in a string

# for charvar in "Python":
#     print(charvar)


#nested loop examples
for i in range(3):
    for j in range(2):
        print(f"({i},{j})")




#iteration over dictionary items
person={"name":"Ram Bahadur","age":30,"city":"Dhangadi"}
for key,value in person.items():
    print(f"{key}:{value}")

#using enumerate to get both index and value
colors = ["red","green","blue"]
for index,color in enumerate(colors, start=1): # enumerate(colors)
    print(f"Index:{index},Color:{color}")

    # print("Index:{},Color:{}".format(index,color))



for index,charvar in enumerate("Python"):
    print(f"Index:{index},Cahracter:{charvar}")