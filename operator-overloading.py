#Here in this program I am overlading the function [__add__]
class operat:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
       #s3=operat(m1,m2) 
       #not necessary
        return m1,m2

s1 = operat(43,87)
s2 = operat(54,62)
w=s1+s2
print(w)

