
f = open(r"C:\Users\2k23a\OneDrive\Documents\#Important\Coding\Artificial Intelligence\Python\05\sample.txt","r")
data = f.read()
print(data)
f.close()
f = open(r"C:\Users\2k23a\OneDrive\Documents\#Important\Coding\Artificial Intelligence\Python\05\sample.txt","w")
data = f.write("Updated New data")
print(data)
with open("sample.txt","r") as f:
    print(f.read())