x = int(input())
a = x // 100
b = x // 10 % 10
c = x % 10
d = a*b*c
e = a+b+c
print(a+b+c <= 99, "a+b+c<=99")

print(a * b * c >= 100, "a * b * c >= 100")

print(a > d, "больше ли?")
print(e % 5 == 0, "e%5==0")
print(x % e == 0, "x%e==0")



