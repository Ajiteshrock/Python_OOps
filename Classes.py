class Ajitesh:
    def aj(self,name,height):
        self.name= name 
        self.height = height
        #print(self.name,self.height)  

    def show(self):
        print(self.name+"'s height is "+str(self.height))
        
Aj1= Ajitesh()
Aj1.name = "Ajitesh Mishra"
Aj1.height = 5.9  #instance attribute
Aj1.show() #calling with object
Ajitesh.show(Aj1) # calling the function with class name


