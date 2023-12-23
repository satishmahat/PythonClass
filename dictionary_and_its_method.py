# dictionary means mapping i.e it will always comes in key value pair
# in js, it is known as object and json

player={
    'first_name':'lional',
    'last_name':'messi',
    'age':'35',
    'height':5.7
}
print(player.keys())
print(player.values())
print(player.items())   #prints tuples of all items
print(player['first_name'])
print(player['last_name'])

player={
    'first_name':'lional',
    'last_name':'messi',
    'age':'35',
    'height':5.7,
    'associates':['argentina','barcelona','PSG']
}

print(player['associates'])
print(player['associates'][-2])
print(player['associates'][0])




# Creating new dictionary
d={}
print(type(d))
d['name']='Satish'
d['age']=20
print(d)



# Nesting of dictioary
test={
    'key1':{'nestkey':{'subnestkey':'hello'}}
}
print(test['key1']['nestkey']['subnestkey'])
print(test['key1']['nestkey'])
print(test['key1'])
print(test.values())

