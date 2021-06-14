class Ajitesh:
 
    surname= "Mishra" # It is common for all the objects
    def __init__(self,name,height):
        self.name= name +" "+ self.surname
        #print(self.name)
        self.height = height
        
    def show(self):
        print(self.name +"'s height is "+str(self.height))

    def show_name(self):
        return self.name



Aj1= Ajitesh("Sajal",5.9)
Pj1 = Ajitesh('Pranjal',5.6)
Aj1.show()
Pj1.show()


