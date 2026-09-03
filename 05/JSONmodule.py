import json
#json strings operation
py_obj = {"name":"Shradha",
          "isTeacher":True,
          "studnt": None}
jason_string = json.dumps(py_obj)
print(jason_string)
print(type(jason_string))
json_str = '{"name":"Shradha","isTeacher":true,"studnt": null}'
pyt_obj  = json.loads(json_str)
print(pyt_obj)
print(type(py_obj))
#json file operations
with open (r"C:\Users\2k23a\OneDrive\Documents\#Important\Coding\Artificial Intelligence\Python\05\data.json",'r') as f:
    print(f)
    pyth_obj = json.load(f)
    print(pyth_obj)
    print(type(pyth_obj))
with open (r"C:\Users\2k23a\OneDrive\Documents\#Important\Coding\Artificial Intelligence\Python\05\data.json",'w') as f:
    json_strin = json.dump(py_obj,f,indent=0,sort_keys=True)
    print(json_strin)