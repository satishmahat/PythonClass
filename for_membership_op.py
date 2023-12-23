city=['ktm','pkr','npj','dhr']
dist=['ktm','kaski','banke','unknown']
test=[city,dist]

for item in city:   # 'in' is a membership operator returns true or false 
    print(item)

print('ktm' in city)
print('ktm' not in city)

one='pkr'
check=one in city
print(check)
