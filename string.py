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
"""
