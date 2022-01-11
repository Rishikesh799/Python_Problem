"""-----------------------------------DICT PROB----------------------------------------------------------------
#1. Write a Python script to sort (ascending and descending) a dictionary by value.

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(sorted(d.items(),key=lambda x:x[1],reverse=True))
#ascending==[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
#descending==[(3, 4), (4, 3), (1, 2), (2, 1), (0, 0)]
---------------------------------------------------------------------------------------------------------------
#2. Write a Python script to add a key to a dictionary.
d= {0: 10, 1: 20}

d[5] = 90        ### one way to add
d.update({4:60}) ### 2nd way to add
print(d)
#OUTPUT=={0: 10, 1: 20, 5: 90, 4: 60}
----------------------------------------------------------------------------------------------------------------
#3. Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
d={}
#d.update(dic3)
#d.update(dic1)
#d.update(dic2)
#print(d)
#OUTPUT=={5: 50, 6: 60, 1: 10, 2: 20, 3: 30, 4: 40}
##by using for loop---------------------------------------------------------------------------------------------
for i in dic1,dic2,dic3:
    d.update(i)
print(d)
OUTPUT=={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
---------------------------------------------------------------------
#4. Write a Python script to check whether a given key already exists in a dictionary.

x={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(10 in x)
print(5 in x)

#OUTPUT==False
         True
----------------------------------------------------------------------------------------------------------------
#5.Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30}
for i in d:
    print(i,"==",d[i])
OUTPUT==x == 10
        y == 20
        z == 30
------------------------------------------------------------------------------------------------------------------
#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

d={}
for i in range(1,11):
    d.update({i:i*i})
print(d)
OUTPUT=={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
----------------------------------------------------------------------------------------------------------------
#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.

print({i:i**2 for i in range(1,16)})
OUTPUT=={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
---------------------------------------------------------------------------------------------------------------
#8.Write a Python script to merge two Python dictionaries.

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d={}
for i in d1,d2:
    d.update(i)
print(d)
#OUTPUT==={'a': 100, 'b': 200, 'x': 300, 'y': 200}
-------------------------------------------------------------------------------------------------
#9. Write a Python program to sum all the items in a dictionary.

s=0
for i in x.values():
    s=s+i
print(s)
-----------------------------------------------------------------------------------------------------
#10. Write a Python program to multiply all the items in a dictionary.

x={'a': 100, 'b': 200, 'x': 300, 'y': 200}
s=1
for i in x.values():
    s=s*i
print(s)
OUTPUT==1200000000
-------------------------------------------------------------------------------------------------------------------
#11. Write a Python program to remove a key from a dictionary.
x={'a': 100, 'b': 200, 'x': 300, 'y': 200}
for i in x:
    print("keys ==",i)
------------------------------------------------------------------------------------------------------------------
#12.Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values=[5,8,6]
d={}
for i,j in zip(keys,values):
    d[i]=j
print(d)
OUTPUT=={'red': 5, 'green': 8, 'blue': 6}
--------------------------------------------------------------------------------------------------------------------
#13. Write a Python program to sort a given dictionary in reverse order by key.
x={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
y=sorted(x.items(),key=lambda i:i[0],reverse=True)
print(y)
OUTPUT==[(10, 100), (9, 81), (8, 64), (7, 49), (6, 36), (5, 25), (4, 16), (3, 9), (2, 4), (1, 1)]
-------------------------------------------------------------------------------------------------------------------
#14. Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
x=[i for i in my_dict.values()]
print("maximum value=",max(x),"\nminimum value=",min(x))
OUTPUT==maximum value= 5874
minimum value= 500
-------------------------------------------------------------------------------------------------------------------
#15.Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

d={}
for i,j in zip(d1,d2):
    if i==j:
        x=d1[i]+d2[j]
        d.update({i:x})
    else:
        d.update({i:d1[i]})
        d.update({j:d2[j]})
print(d)
OUTPUT=={'a': 400, 'b': 400, 'c': 300, 'd': 400}
------------------------------------------------------------------------------------------------------------------
#16.Write a Python program to print all unique values in a dictionary.

x=[{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
k=[]
for i in x:
    for j in i.values():
        k.append(j)
print(set(k))
OUTPUT=={'S002', 'S001', 'S007', 'S009', 'S005'}
---------------------------------------------------------------------------------------------------------------
#17.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
x={'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

d=sorted(x.items(),key=lambda i:i[1],reverse=True)
for i in d[:3]:
    print(i[0],end=" ")
#OUTPUT==b e c
"""




















