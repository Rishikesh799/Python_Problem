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
