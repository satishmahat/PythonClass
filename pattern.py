
#code1

n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end='')
#     print()


#code2
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()