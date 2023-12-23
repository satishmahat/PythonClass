# length of string

a=input("enter a word : ")
c=len(a)
print(c)
if c%2==0:
    print("the word",a,"has even number of character")
else:
    print(a,"has odd number of character")


#WAP to find vowel or not

x=input("enter a character : ").lower()
print(x)
if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
    print(x,"is a vowel")
else:
    print(x,"is a consonent")



