n = input("Enter the String ")
count = 0
for var in n:
    if(var=='a' or var=='i' or var=='o'or var == 'e' or var=='u'):
        count+=1
print(count)