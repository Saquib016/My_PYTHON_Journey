# #Question 1
# x = input("Enter the String  = ")

# l = len(x)
# for i in range(l//2):
#     if(not(x[i] == x[l-i-1])):
#         print(f"{x} is not  Palindrome")
#         break

# else:
#     print(f"{x} is a Palindrome")

#Question 2
# li = [1,4,3,5,7] 
# sum = 0 
# for i in li:
#     sum+=i
# print(f"Average of Given list = {sum/len(li)}")

# #Question 3
# list1 = [1,2,7]
# list2 = [2,4,5]
# for i in range(len(list2)):
#     list1.append(list2[i])
# list1.sort()
# print(f"Result  = {list1}")

# #Q04
# tup = (3,4,2,5,6,67,7,5,7,5,4,3)
# tup1 = ()
# tup2 = ()
# for i in tup:
#     if(i%2==0):
#         tup1 = tup1+(i,)
#     else:
#         tup2 = tup2+(i,)
# print(f"Even Tupple = {tup1} & odd Tupple = {tup2}")
# #Q05
# k = {"Arya":"60",
#      "Shikhar":"69",
#      "S":"65",
#      "a":"97",
#      "M":"45",
#      "f":"68"}
# P = input("Enter the Program \n Press A - Add a student \n Press B - Update marks\n Press C - Search for a student\n Press D - Display all students and marks")
# if(P=='A'):
#     x = input("Enter Student name = ")
#     y = int(input("Enter Marks = "))
#     k.update({"x":"y"})
# elif(P=='B'):
#     x = input("Enter Student name = ")
#     y = int(input("Enter New Marks = "))
#     k.update({"k[x]":"y"})
# elif(P=='C'):
#     x = input("Enter Student name = ")
#     y = int(input("Enter New Marks = "))
#     k.update({"k[x]":"y"})
#Question 10
str = input("Enter the String = ")
st= set()
for i in range(len(str)):
    st.add(str[i])
    
print(f"{st} and the count of unique character is {len(st)}")
