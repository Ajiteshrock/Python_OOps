s = input()
p = input()
new = input()
index = s.index(p)
print(index)
s = s.replace(p,new)
for i in s:
    if i==new and s.index(i) == index:
        continue
    elif i==new and s.index(i) != index:
        s = s.replace(new,p,1)
     
print(s)
