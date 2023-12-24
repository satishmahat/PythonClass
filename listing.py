# list is a collection of elements and it is similar to an array in other
#list are mutauable i.e elements inside a list can be changed
# indexing always starts from '0'

# Mountain=['Sagarmatha','Dhaulagari','Annapurna','Lhotse','Makalu']
# print(type(Mountain))
# print (Mountain)
# print(len(Mountain))


# indexing and slicing


# print(Mountain[2:])
# print(Mountain[0:3])
# print(Mountain[-1]) #use to print last position element
# print(Mountain[-3:-1])
# print(Mountain[:])


#list methods

# append()
# pop()
# sport()
# reverse()


# Mountain.append('Kilimanjaaro')
# print(Mountain)

# Mountain.pop()
# print(Mountain)

# Mountain.pop(2)
# print(Mountain)

# Mountain.sort()
# print(Mountain)

# Mountain.reverse()
# print(Mountain)





# Nested list => listing inside list

Barcelona=['messi','neymar','suarez']

PSG=['messi','mbappe','neymar']

matrix=[Barcelona,PSG]
print(matrix)
print(matrix[1])
print(matrix[0])
print(matrix[1][2])




city=['ktm','pkr','npj','dhr']
dist=['ktm','kaski','banke','unknown']
test=[city,dist]
print(test[1][3])

print(dist[:-2])
