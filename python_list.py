l = ["Ajay","25",'Delhi',"Amit","27",'Gurgaon','sumit','17','Noida']
l_names = []
l_age  = []
l_cities = []
length = len(l)

for i in range(0,length-2,3):
    l_names.append(l[i])
    l_age.append(l[i+1])
    l_cities.append(l[i+2])

print(l_names,l_age,l_cities)