def fact(n):
    i=1
    fact=1
    while (i<=n):
        fact*=i
        i+=1
    return fact
n = int(input("Enter the Number = "))

print(fact(n))