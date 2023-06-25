#write a line into writefile.txt file
obj = open('writefile.txt', 'w')
obj.write('hello world')
obj.close()
#now read the file
obj = open('writefile.txt', 'r')
print(obj.read())
