# unordered 
# unchangable and no duplicates

thisset1={"apple","banana","cherry","apple"}

thisset2={"one","two","three"}

for x in thisset1:
    print(x)

thisset1.update(thisset2)
print(thisset1)

thisset3=thisset1.union(thisset2)
print(thisset3)

thisset2.clear()
print(thisset2)

#typecasting in set

set1=set(['Sagarmatha','Dhaulagari','Annapurna','Lhotse','Makalu']) 
print(set1)

# set1.add(['add1','add2']) #cannot add list
set1.add("add1")

# set1[1]="hello"
print(set1)



#union

player={"subash","santosh","kiran"}
film={"karan","arjun"}
man={"dipesh","ram"}


aswell= player.union(film)
print(aswell)


aswell=player|man
print(aswell)



#intersection

player1={"subash","santosh","kiran"}
player2={"subash","satish","kiran"}


player1= player1 & player2
print(player1)



abc1=set()
abc2=set()

for i in range(5):
    abc1.add(i)

for i in range(3,9,2):  
    abc2.add(i)

print(abc1)
print(abc2)


