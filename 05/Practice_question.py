data = True
i=0
with open(r"C:\Users\2k23a\OneDrive\Documents\#Important\Coding\Artificial Intelligence\Python\05\sample.txt",'r') as f:
    while data:
        data = f.readline()
        if("Chal" in data):
            print(f"Found at {i}nd line")
            break
        i+=1
        

