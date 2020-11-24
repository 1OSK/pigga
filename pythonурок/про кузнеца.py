a = int(input())
b = int(input())
c = int(input())
r = int(input())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
SK = 3.14*r**2
print(SK <= S)