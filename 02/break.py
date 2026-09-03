# i=1
# while(i<=10):
#     if(i==6):
#         break
#     print(i)
#     i+=1;
color = input("Enter the Color = ")
match color:
    case 'green':
        print("Go")
    case 'yellow':
        print("Look")
    case 'Red':
        print("Stop")
    case _:
        print("Wrong Color")