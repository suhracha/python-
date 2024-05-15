age = int(input('enter age to know the rate of interest for loan: '))

if age<18:
    print('no loan available')
elif age>=18 and age<=21:
    print('0.5%')
elif age> 21 and age<=45:
    print('6%')
elif age> 45 and age<60:
    print('4.5%')
else:
    print('no loan available')