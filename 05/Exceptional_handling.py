try:
    x= int(input("Enter the Number = "))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by Zero is not Allowed")
except ValueError:
    print("Invalid Format")
else:
    print(f"The value after divided by {x} is {ans}")