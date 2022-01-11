"""
s="GEEGEEKSKS"
a="GEEKS"

while True:
    if a in s:
        x=s.find(a)
        y=s[:x]+s[(x+len(a)):]
        if y == "":
            print("yes")
            break
        else:
            s=y
    else:
        print("no")
        break
------------------------------------------------------------------------------------------------
x=["gee","geee","ge","g"]
y=sorted(x,key=lambda x:x.count("e"),reverse=True)
print(y)
-----------------------------------------------------------------------------------------
x="abc$$cd"
d=[]
e=[]
for i in x:
    if i.isalpha():
        d.append(i)
    else:
        e.append(i)
#print("".join(d+e))
#print("".join(e))

print("".join([i for i in x if i.isalpha()]))
-----------------------------------------------------------------------------------

x=[(4,5,5,4),(4,5,5,4),(5,4,3)]
k=5
n=2
d=[]
for i in x:
    if i.count(k)==n:
        d.append(i)
print(d)

#print([i for i in x if i.count(k)==n ])
"""









