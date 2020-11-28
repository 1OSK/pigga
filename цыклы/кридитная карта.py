number=int(input())
numberstring=str(number)
sum=0
if len(numberstring)<14 or len(numberstring)>19:
    print("не номер")
else:
    k=number%10
    number//=10
    numberstring=str(number)[-1]
    length=len(numberstring)
    for i in range(0,length):
        if i%2==0:
            cifra=int(numberstring[i])
            cifra*=2
            if cifra>9:
                cifra=cifra//10+cifra%10
            sum+=cifra
        else:
            sum+=int(numberstring[i])
    print(k==10-sum%10)