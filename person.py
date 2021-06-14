import math
class Person:
      def __init__(self , name , height:int , weight:int , bmi=0 , bmi_status=""):
            self.name = name 
            self.height  = height 
            self.weight = weight 
            self.bmi = bmi
            self.bmi_status = bmi_status
      def calculatebmi(self):
            self.bmi = math.ceil(int(self.weight) / int(self.height) ** 2)


class Society:
      def __init__(self , bmi_dict , person_list):
            self.bmi_dict = bmi_dict
            self.person_list = person_list


      def calculatebmiandstatusbyname(self , name): 
            new_ = []
            flag =0
            
                 
            for i in self.person_list:
                if i.name == name:
                   flag =1
                   ''' for j in self.bmi_dict.keys():
                        if (int(i.bmi) <= int(self.bmi_dict[j][0])) and (int(i.bmi) >= int(self.bmi_dict[j][1])):
                            print("sumbitting bmi status")
                            i.bmi_status = j'''
            
            if flag == 1:
                for i  in self.person_list:
                    for j in self.bmi_dict.keys():
                            if (int(i.bmi)>=int(self.bmi_dict[j][0])) and (int(i.bmi)<=(int(self.bmi_dict[j][1]))):
                                i.bmi_status = j
                return True
            else:
                 return False
 
      def show_invalid(self , number):
            l= []
            l1 =[]
            for i in self.person_list:
                if (int(i.bmi) >= int(number)):
                    l.append(i.name)
                    l1.append(i.bmi)
                     
            return l , l1
        
def main():
    no = int(input())
    li=[]
    for i in range(no):
        name = input()
        height = input()
        weight = input()
        p = Person(name ,height,weight)
        p.calculatebmi()
        li.append(p)
    no1 = int(input())
    d={}
    for i in range(no1):
        t=[]
        string = input()
        up_limit = int(input())
        lw_limit = int(input())
        t.append(up_limit)
        t.append(lw_limit)
        if string not in d.keys():
            d[string] = t
    S = Society(d,li)
    n = input()
    n = int(input())
    if S.calculatebmiandstatusbyname(name):
        for i in S.person_list:
            if i.name == name:
                 print(str(i.bmi)+" "+i.bmi_status)

    p , k = S.show_invalid(n)
    
    for i in range(len(k)):
        print(p[i],k[i])
main()