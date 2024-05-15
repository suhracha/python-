class A:
    def disp(self):
        print('this is parent class')
class B(A):
    def disp(self):
        print('this is child class')

# obj = A()
# obj.disp()
obj2 = B()
obj2.disp()