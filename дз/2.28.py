import math
a=float(input("большее основание "))
b=float(input('угол при большем основании '))
d=float(input("меньшее основание "))
c=b*math.pi/180
print("угол при меньшей стороне ", c)


print((a**2-d**2)/4*math.tan(c))