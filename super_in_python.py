#Here we determine the concept of super() keyword
class father:

    def __init__(self):
        self.name= "Ajitesh" 
        print("in A's constructor")

    def show(self):
        print("Your name is",self.name)
    def prob1(self):
        print("this is prop 1 ")
    def prop2(self):
        print("this is prop 2 ")

class child(father): #the basic syntax for inheritance 
    
    def __init__(self):
        print("in the consturctor of b")
        print("calling A's constructor")
        super().__init__()
    def prob3(self):
        print("this is prop 3 ")
    def prop4(self):
        print("this is prop 4 ")

c = child()
 # now child inherted all properties from
          # father so he can use the all the four properties as well
#concept of constructor is this , when we creat a constructor in super 
# or parent class but make a object of child class so when this
#  object created itself so it will call the constructor of parent
#because in child class there is no contructor so at the first sight i
#it will look in own class to find constructor if there were not 
# then in parent class but if we make in child class it will call its 
#own constructor but if in this situation we want to call parent 
#class constructor then we have to use ""Super()"" keyword as above