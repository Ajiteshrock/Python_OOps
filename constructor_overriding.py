class Father:
    def __init__(self):
        self.money = 100
        print("father's contructor running")

class Child(Father):
    def __init__(self):
        self.money = 200
        print("Child's contructor running")

s = Child() # will give the output 'child's consturctor running'

class Child1(Father):
    def show(self):
        return "Ok Python"

s1 = Child1() # will give the output 'father's contructor running'
