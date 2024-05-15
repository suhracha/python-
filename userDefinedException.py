class myExcep(Exception):
    def __init__(self,message):
        self.message = message

def divideNum(a,b):
    if b==0:
        raise myExcep("Division by zero is not allowed!")
    return a/b

try:
    n1 = int(input('Enter num1= '))
    n2 = int(input('Enter num2= '))
    res = divideNum(n1,n2)
    print(res)
except myExcep as e:
    print("exception: ", e.message)