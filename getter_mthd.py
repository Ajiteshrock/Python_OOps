class Student:
    def __init__(self,mh,ph,ch):
        self.mh= mh
        self.ph= ph
        self.ch= ch
        

    def show_avg(self):
        avg=(self.mh+self.ph+self.ch)/3
        self.avg=avg
        print(avg)

    def get_mh(self):
       print("marks in maths"+str(self.mh))

    def compare(self,other):
        
        if(self.avg>other.avg):
            return True
        else:
            return False

    

    
Aj1= Student(86,88,96)
print("showing average marks")
Aj1.show_avg()


Pb1= Student(96,96,96)
Pb1.show_avg()
'''if(Aj1>Pb1):
    print("yes")''' #this will give error because
                    # we can not campare instances directly 
                    # so for that we have to make a function
print("comparing")
if Aj1.compare(Pb1):
     print("AJitesh has heigher marks ")
else:
    print("Prabodh has heigher marks")
                    

