#multilevel inhreritance
class grandfather:
    
    def prop1(self):
        print("this is prop 1 ")
    def prop2(self):
        print("this is prop 2 ")

class father(grandfather): #the basic syntax for inheritance 
    
    def prop3(self):
        print("this is prop 3 ")
    def prop4(self):
        print("this is prop 4 ")


class child(father): #the basic syntax for inheritance 
    
    def prop5(self):
        print("this is prop 5 ")
    def prop6(self):
        print("this is prop 6 ")

c = child()
c.prop1() # now child inherted all properties from
c.prop3()
c.prop5()         # father  and grandfather so he can use the all the six 
          # properties as well