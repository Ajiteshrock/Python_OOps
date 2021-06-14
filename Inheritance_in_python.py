#single inheritance
class father:
    
    def prob1(self):
        print("this is prop 1 ")
    def prop2(self):
        print("this is prop 2 ")

class child(father): #the basic syntax for inheritance 
    
    def prob3(self):
        print("this is prop 3 ")
    def prop4(self):
        print("this is prop 4 ")

c = child()
c.prob1() # now child inherted all properties from
          # father so he can use the all the four properties as well