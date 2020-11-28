a=7525
max=7524
b=0
for i in range(a, 13486):
    if i%7==0 and i%6!=0 and i%9!=0 and i%14!=0 and i%21!=0:
        b=b+1
        if i%7==0 and i%6!=0 and i%9!=0 and i%14!=0 and i%21!=0 and a>max:
            max=i
print(b, max)
