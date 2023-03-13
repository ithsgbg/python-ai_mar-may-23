class A:
    def __init__(self, value):
        print('A init')
        self.value = value
        
class B(A):
    def __init__(self, value):
        super().__init__(value)
        print('B init')
        self.value *= 2
    
class C(A):
    def __init__(self, value):
        super().__init__(value)
        print('C init')
        self.value -= 3
        
class D(B, C):
    def __init__(self, value):
        super().__init__(value)        
        print('D init')
        
d = D(10)

print(d.value)
print(D.mro())