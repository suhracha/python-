sett = {'j','k','l','m'}
print(sett)

sett.add('n')
print(sett)

sett.discard('l')
print(sett)

sett.remove('n')
print(sett)

p = sett.copy()
print("sett: ",sett, "p: ", p)

sett.clear()
print(sett)
