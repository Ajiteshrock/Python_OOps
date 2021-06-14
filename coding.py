number = int(input())
l=[]
ct=1
min_number=0
count=1
import math
for i in range(2,number//2+1):
    if number % i == 0:
        count+=1
        l.append(i)
if count<=1:
    print("Not Possible")
else:
    for i in range(len(l)-1):
        product = l[i] * l[i+1]
        new_number = str(l[i]) + str(l[i+1])
        new_number = int(new_number)
        if ct==1 and product == number:
            min_number = new_number
            ct+=1
        elif ct>1 and product==number:
            if min_number > new_number:
                min_number= new_number

    print(min_number)