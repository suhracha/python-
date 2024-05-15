with open('first.txt','r') as f:
    contents= f.readline()
with open('second.txt', 'w') as f1:
    f1.write(contents)