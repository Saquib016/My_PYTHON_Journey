username = input("Enter the USer NAME = ")
password = input("Enter the Password = ")
if(username == "admin"):
    if(password =="pass" ):
        print("Login Sucessful")
else:
    if(username!="admin"):
        print("Wrong UserNAme")
    else:
        print("Wrong password")