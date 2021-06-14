class Ajitesh:
    def __init__(self):
        self.name= 'Ajitesh' '''This is contructor for the object Aj1'''
        self.height = 60
        

    def show(self):
        print(self.name+"'s height is "+str(self.height))

    def upadte(self): 
        self.height=float(input("enter the new height"))
Aj1= Ajitesh()
Aj1.name = "Ajitesh Mishra"
Aj1.height = 5.9  #instance attribute
Aj1.show() #calling with object before updation 
#Ajitesh.show(Aj1) # calling the function with class name
print("after updation the height is")
Aj1.upadte()
Aj1.show() #it will show the output with after updation of height
