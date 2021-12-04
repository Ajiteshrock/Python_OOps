class A:
    def show(self):
        print("Called A")

class B(A):
    
    def show(self):
        print("Called B")

class C(B):
    pass 

c = C()
print(c.show())