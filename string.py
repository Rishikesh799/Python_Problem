"""
x="character"
print([i for i in x])
-------------------------------------------------------------------------------------------
x="Split me, please"
y=x.split(",")
print([i for i in y])
out put==
        ['Split me', ' please']
---------------------------------------------------------------------------------------------
l = ['hello', 'world']
o = "this string contains the world hello"
p = "this string contains no relevant words"
def game(x,y):
    for i in x:
        if i in y:
            print("True")
        else:
            print("False")


game(l,o)
game(l,p)
-------------------------------------------------------------------------------------------------
x="character"
print([i for i in x])
------------------------------------------------------------------------------------------
x=['c', 'h', 'a', 'r', 'a', 'c', 't', 'e', 'r']
y="".join(x)
print(y)
-----------------------------------------------------------------------------------------------
t=tuple("rishikesh")
print(list(t))
print("".join((list(t))))
print(len((list(t))))
---------------------------------------------------------------------------------------------
#check whether string pallidrome or symmetric
def pallidrome(x):
    if x==x[::-1]:
        print("pallidrome")
    else:
        print("not pallidrome")
def symmetrical(x):
    y=int(len(x)/2)
    print(y)
    if x[:y]==x[y:]:
        print("symmetrical")
    else:
        print("not symmetrical")
n="amaama"
pallidrome(n)
symmetrical(n)

pallidrome
3
 symmetrical
---------------------------------------------------------------------
#Reverse the words in string
x="my name is rishikesh"
y=x.split()
print(" ".join(y[::-1]))

rishikesh is name my
-------------------------------------------------------------------------
#Avoid spaces in string:
x="my name is rishikesh"
d=[]
for i in x:
    if i.isalpha():
        d.append(i)
print(len(d))
print("".join(d))
17
mynameisrishikesh
------------------------------------------------------------------------------------------------------
#python programe to even length words.

x="my name is rishikesh"
y=x.split()

for i in y:
    if len(i)%2==0:
        print(i,end=" ")

my name is
------------------------------------

##Half of sring create upper case.
x="geek"
y=int(len(x)/2)
print(x[:y].upper()+x[y:])
GEek
-------------------------------------------------------------------
-----------------
x="geek"
d=[]
for i in range(len(x)):
    if i==0 or i==len(x)-1:
        d.append(x[i].upper())
    else:
        d.append(x[i])
print(("".join(d)))

print(x[0].upper()+x[1:len(x)-1]+x[len(x)-1].upper())
GeeK
GeeK
-----------------------------------------------------------------------------
x="abcdef"
y="defghia"
d=[]
for i in x:
    if i in y:
        d.append(i)
    else:
        pass
print("common chr in both str is :",d,",And their count is :",len(d))

common chr in both str is : ['a', 'd', 'e', 'f'] ,And their count is : 4

----------------------------------------------------------------------------
x="vic"
from itertools import permutations
y=permutations(x)
for i in y:
        print("".join(i))
---------------------------------------------------------------------------------------
x={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
y="zero nine one two eight"
b=y.split()
s=[]
for i in b:
    s.append(str(x[i]))
print("".join(s))
-------------------------------------------------------------------------------------------------
### Word location in string
x="zero nine one two eight"
y="nine"
c=x.split()
if y in c:
    print(c.index(y)+1)
--------------------------------------------
x="GeeksforGeeks"
d=2
def rotation(x):
    y=x[:d]
    j=x[len(x)-d:]
    print("for left rotation:",x[d:]+y)
    print("For right rotation:",j+x[:len(x)-d])
rotation(x)
-------------------------------------------------------
x="geeks_for_geeks"
print(x.replace("_",""))
y=x.split("_")
print("".join(y).upper())
"""
