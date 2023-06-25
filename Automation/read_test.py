obj = open('./DemoProject/Automation/readfile.txt', 'r')
# read all data from the file
print(obj.read())

print()

# real all data from the file
print(obj.read(12))

# read one line from the file
print(obj.readline())

# read all characters from file and display 1 by 1
for i in obj.read():
    print(i)

# read all data from line by line
z = obj.readline()
while (z):
    print(z)
    z = obj.readline()
