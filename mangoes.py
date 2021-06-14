a = int(input())
m = int(input())
rs = int(input())
if a>m:
    rs = rs - (a-m)
elif m>a:
    rs = rs + (m-a)
print(rs)

