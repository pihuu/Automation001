obj=open('readfile.txt','r')
#print(obj.read())
#tell function is used to determine the current position of the file pointer
print(obj.tell())
obj.readline()
print(obj.tell())
#seek function is used to the specific position of the file
print(obj.seek(4))
print(obj.tell())



