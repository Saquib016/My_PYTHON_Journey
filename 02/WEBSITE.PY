username = input("Enter USerNAme = ")
passwo = input("Enter PAssword = ")
if (username == 'admin' and passwo == '123xyz') :
    print("Login Successful")
elif (username!='admin' and passwo =='123xyz') :
    print("Username not Matched")
elif (username=='admin' and passwo!='123xyz') :
    print("Password Invalid")
else:
    print("Not Valid Username and Password")
