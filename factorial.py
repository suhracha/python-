n = int(input('Enter the number whose factorial you want: '))
f = 1
if n <0:
    print('invalid')
else:
    for i in range(1, n + 1):
        f = f * i
    print(f)


