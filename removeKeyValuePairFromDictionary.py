dict = {0: 20,1: 2.34,2: 'hru'}
print(dict)

#pop
print(dict.pop(1))
print(dict)

#popitem 
dict = {0: 20,1: 2.34,2: 'hru'}
print(dict.popitem())
print(dict)

#clear 
dict = {0: 20,1: 2.34,2: 'hru'}
dict.clear()
print(dict)

#delete item (extra)
dict = {0: 20,1: 2.34,2: 'hru'}
dict.__delitem__(0)
print(dict)

#del 
dict = {0: 20,1: 2.34,2: 'hru'}
del dict[0]
print(dict)

