"""-********------------TUPLE PROBLEMS----------------**********
#1. Write a Python program to create a tuple.
x=()
print(x)
-------------------------------------------------------------------
#2. Write a Python program to create a tuple with different data types
x=(1,"str","3i+j",5.5)
print(x)
-------------------------------------------------------------------
##3. Write a Python program to create a tuple with numbers and print one item.
x=5,20,30,15.2,96
print(x)
print(x[0])
---------------------------------------------------------------------
#4. Write a Python program to unpack a tuple in several variables.
x = 5,60,80,"ram",12.5
l1,l2,l3,l4,l5 =x
print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
-----------------------------------------------------------------
#5. Write a Python program to add an item in a tuple.
x =5,60,80,"ram",12.5
print(x)
y = list(x)   ### convert above x in list
print(y)
y.append(5)   ### use method of list to add element in list
print(y)
x=tuple(y)    ### convert the list in tuple
print(x)
---------------------------------------------------------------------
#6. Write a Python program to convert a tuple to a string.
x ="ved","ram","sham"
print(x)
print("".join(x))
----------------------------------------------------------------------
#7. Write a Python program to get the 4th element and 4th element from last of a tuple.

x =5,60,80,"ram",12.5
print(x[3])
print(x[-4])
------------------------------------------------------------------------
#8. Write a Python program to find the repeated items of a tuple. ********************
x = 2,3,2,6,2,8,1,9,2
d=[]
for i in x:
    if x.count(i)>1:
        if i not in d:
            d.append(i)
            print(i,"count is ",x.count(i))
--------------------------------------------------------------------------
#10. Write a Python program to check whether an element exists within a tuple.
x = 2,3,2,6,2,8,1,9,2
print(8 in x)
print(2 in x)
---------------------------------------------------------------------------
#11. Write a Python program to convert a list to a tuple
x = [2,3,2,6,2,8,1,9,2]
print(tuple(x))
---------------------------------------------------------------------------
#12. Write a Python program to remove an item from a tuple.
x = 2,3,2,6,2,8,1,9,2
#y=x[:x.index(6)]+x[x.index(6)+1:] ### by using slicing and indexinf we remove the element
#print(y)
 ## by using list
z=list(x)
z.remove(8)
print(tuple(z))
-----------------------------------------------------------------------------------
#13. Write a Python program to slice a tuple
x = 2,3,2,6,2,8,1,9,2
y=x[:x.index(6)]
print(y)
-----------------------------------------------------------------------------------
#14. Write a Python program to find the index of an item of a tuple.
x = 2,3,2,6,2,8,1,9,2
print(x.index(8))
-----------------------------------------------------------------------------------
#15. Write a Python program to find the length of a tuple.
x = 2,3,2,6,2,8,1,9,2
print(len(x))
------------------------------------------------------------------------------------
#16. Write a Python program to convert a tuple to a dictionary.

x = 2,3,2,6,2,8,1,9,2
s={}
for i in x:
    s[i]= x.count(i)
print(s)

a= ((5,9),(4,7))
print({i:j for i,j in a })
------------------------------------------------------------------------------------
#17. Write a Python program to unzip a list of tuples into individual lists.
a= ((5,9,6),(4,7,9))
d=[]
for i,j,k in a:
    d.append(i)
    d.append(j)
    d.append(k)
print(d)
-------------------------------------------------------------------------------------
#18. Write a Python program to reverse a tuple.
x = 2,3,2,6,2,8,1,9,2
print(x[::-1])
print(tuple(reversed(x)))
---------------------------------------------------------------------------------
#19.Write a Python program to convert a list of tuples into a dictionary.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
k={}
for i,j in l:
    x=k.setdefault(i,[])
    x.append(j)
print(k)
---------------------------------------------------------------------
#20. Write a Python program to print a tuple with string formatting.
x = (100, 200, 300)
print("this is a tuple {}".format(x))
------------------------------------------------------------------------
#21. Write a Python program to replace last value of tuples in a list.
x = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
c=[]
for i in x:
    y=list(i)
    y[2]=100
    c.append(tuple(y))
print(c)
--------------------------------------------------------------------------------------
#22. Write a Python program to remove an empty tuple(s) from a list of tuples.
x = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
m=[]
for i in x:
    if len(i)!=0:
        m.append(i)
print(m)
### by list comprehension
print([i for i in x if len(i) != 0])
----------------------------------------------------------------------------------------
#23. Write a Python program to sort a tuple by its float element.
x =[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

print(list(sorted(x,key=lambda i:i[1],reverse=True)))  ## for 2nd elment in tuple we checking so take index 1
---------------------------------------------------------------------------------------
#24.Write a Python program to count the elements in a list until an element is a tuple.
x =[10,20,30,(10,20),40]
co=0
for i in x:
    if type(i) is tuple:   ## check the type of i and compare .
        break
    else:
        co=co+1
print(co)
----------------------------------------------------------------------------------------------
#26. Write a Python program calculate the product, multiplying all the numbers of a given tuple
x =(4, 3, 2, 2, -1, 18)
s=1
for i in x:
    s=s*i
print(s)
------------------------------------------------------------------------------------------------
#27. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
x =((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
z=[]
s=0
for i in zip(*x):
    d=sum(i)/len(i)
    z.append(d)
print("Average of tuple in tuple is ",z)
##By list comprehension
print([sum(i)/len(i) for i in zip(*x)])
-------------------------------------------------------------------------------------------
#28. Write a Python program to convert a tuple of string values to a tuple of integer values.
x =(('333', '33'), ('1416', '55'))
k=[]
for i,j in x:
    k.append((int(i),int(j)))
print(tuple(k))
--------------------------------------------------------------------------------------------------
#29. Write a Python program to convert a given tuple of positive integers into an integer.
x =(10, 20, 40, 5, 70)
y="".join(map(str,x))
print(y)
-------------------------------------------------------------------------------------------------------

#30. Write a Python program to check if a specified element presents in a tuple of tuples.
x =(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
for i in x:
    if "White" in i:
        print(True)
        break
    else:
        continue
else:
    print(False)


------------------------------------------------------------------------------------------
#31. Write a Python program to compute element-wise sum of given tuples.
x = [(1, 2, 3, 4),(3, 5, 2, 1),(2, 2, 3, 1)]
c=[]
for i in zip(*x):
    f=sum(i)
    c.append(f)
print(tuple(c))
----------------------------------------------------------------------------------------------------
#32. Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples
x=[(1, 2), (2, 3), (3, 4)]
p=[]
for i in x:
    p.append(sum(i))
print(p)
----------------------------------------------------------------------------------------------------
#33. Write a Python program to convert a given list of tuples to a list of lists.
x =[(1, 2), (2, 3), (3, 4)]
print([list(i) for i in x])
"""


























