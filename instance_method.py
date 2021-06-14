#There are three types of methods in python
#Instance method
#Class methods
#static methods
class Student:
    school = 'Telusko'
    #class_variables

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)//3

    def get_ml(self):
        return self.m1

    def set_m1(self , value):
        self.m1 = value


s1 = Student(1,2,3)
s2 = Student(4,5,6)
print(s1.avg())
print(s2.avg())
#both method called before updatig the values
s2.set_m1(55)
s2.get_ml()
print(s2.avg())
#now s2's m1 value is upadate to 66
