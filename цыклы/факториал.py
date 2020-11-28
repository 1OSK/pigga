n = int(input("n"))
if n > 0:
    for i in range(1, n):
        n = n*i
    print(n)
elif n == 0:
    print("ну тут подругому стичается")
else:
    print("так дела не делаются")
