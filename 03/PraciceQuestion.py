info=[
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]
uniSet = set()
print(type(set))
for val in info:
    uniSet.add(val[1])
print(uniSet)
list = []
for name,subject in info:
    if(subject=="English"):
        print(name) 
dick = {} #Question -  dictionary me add karna hai key and subject ka set banakr ek hi name ke aage sab daal do
for name,subject in info:
    if(dick.get(name)==None):
        dick.update({name: set()}) #add the name if not present then usi name me subject daal do
        dick[name].add(subject)  # add subject to the name
    else:
        dick[name].add(subject) #if already esist so just put the subject into the name
print(dick)