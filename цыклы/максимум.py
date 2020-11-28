n = int(input("n"))
max = -1
for i in range(0, n):
    a = int(input("a"))
    if a > max:
        max = a
print(max)