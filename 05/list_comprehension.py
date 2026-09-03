# Format list = [output iteration condition]
list = [i*i for i in range(6)]
print(list)
lsit2 = [i*i for i in range(10) if i%2==0]
print(lsit2)
# question change -ve to zero
list = [-2,-4,3,5,2,-1]
list = [0 if val<0 else val for val in list]
print(list)