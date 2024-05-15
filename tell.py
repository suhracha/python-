f = open("1.txt", 'r')
print(f.tell())

f = open('1.txt', 'r')
f.seek(5)
print(f.tell())
print(f.readline())
print(f.tell())
