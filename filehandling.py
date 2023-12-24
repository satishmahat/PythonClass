#file operation
'''
1. Open a file
2. Read a file
3. Close a file
'''

#file handling
'''
The key function for working with files in python is the open() function
The open function takes two parameter; filename, and node
There are four different methods(nodes) for opeaning a file:
"r" - Read -Default value.Opens a file reading.error if the file doesnt exit
"a" - Append -opens a file for appending, creates the file if it doesnt exist
"w" - write -opens a file  for writing , creates the fie if it doesnt exist
"t" - opens in text mode
"b" - opens in binary mode
"+" - opens a file for updating (reading & writing)
'''

#syntax

# file1=open('file1.txt','w')
# file1.write("Hello world")
# file1.write("OK")


f=open("one.txt","+w")
f.write("This is the opeaning file ")
f.close()

f=open("one.txt","+a")
f.write("\nThis is second line")
f.close()


# f=open("listing.py",'+a')
# f.write("\nThis is  line")

f=open("one.txt","r")

for line in f:
    print("Line printed through loop is: ",line,end='')
f.close()
print("\nThe file is closed")
