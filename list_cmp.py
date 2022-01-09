"""------------------LIST COMP---------------------------------------
#1.wap find all the no div by 7 in 1to 100

print([i for i in range(1,100) if i % 7==0])
out put==[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
------------------------------------------------------------------------
#2.wap find the no from 1 100 that have a 3 in them

print([i for i in range(1,100) if '3' in str(i)])
OUTPUT ==[3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93]
----------------------------------------------------------------------------------------
#3.count the no of spaces in the string

stg='MMMy name is rishikesh like on'
xy=([i for i in stg if i ==" "])
print(len(xy))
----------------------------------------------------------------------------------
#4.Print the list of all consonants

stg = "My name is vicky"
v = [ 'a','e','i','o','u']
xy =[i for i in stg if i not in v and i != " "]
print(xy)
OUTPUT==['M', 'y', 'n', 'm', 's', 'v', 'c', 'k', 'y']
---------------------------------------------------------------------------
#5.Find the common elements in list without using st or tuple.

a=[1,2,3,4]
b=[2,3,4,5]
x=[i for i in a if i in b]
print(x)

OUTPUT==[2, 3, 4]
------------------------------------------------------------------------------------
#6.Get th only no from string

s = " in 1994 old 55 man  56 dc 23"
w = s.split()
x=[i for i in w if not i.isalpha()]
print(x)
OUTPUT==['1994', '55', '56', '23']
--------------------------------------------------------------------------------------
#7.Print even or odd in boolean form

x=["even" if i % 2 == 0 else "odd"for i in range(10) ]
print(x)
OUTPUT==['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
------------------------------------------------------------------------------------
#8. less than 4 letters words

a= "today is my birthday ok"
w = a.split()
x=[i for i in w if len(i) < 4]
print(x)
OUTPUT==['is', 'my', 'ok']
--------------------------------------------------------------------------------------
#9.Print no contain 6 num from range of 100.

print([i for i in range(1,100) if "6" in str(i)])
OUTPUT==[6, 16, 26, 36, 46, 56, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 76, 86, 96]
---------------------------------------------------------------------------------------
#10.Calculate the no of spaces in string.

string="Practice problems to drill list comprehension"
print(len([i for i in string if i == " "]))
OUTPUT==5
-------------------------------------------------------------------------------------------------------------
#11.find out the all the consonants in the string.

string="Practice problems to drill list comprehension"
print([count for count in string if count not in ["a","e","i","o","u"] and count !=" "])
OUTPUT==['P', 'r', 'c', 't', 'c', 'p', 'r', 'b', 'l', 'm', 's', 't', 'd', 'r', 'l', 'l', 'l', 's', 't', 'c', 'm', 'p', 'r', 'h', 'n', 's', 'n']
-------------------------------------------------------------------------------------------------------------
#12.Wap to find out string which length is less than 5.

string="Practice problems to drill list comprhension"
print([i for i in string.split() if len(i)< 5 ])
OUTPUT==['to', 'list']
-----------------------------------------------------------------------------------------------------
#13.Wap to create dict of word and length of word.

string="Practice problems to drill list comprhension"
print({word : len(word) for word in string.split()})
------------------------------------------------------------------------------------------------------
#14.
print([(i,j) if i % 2 == 0 else (i+1,j) for i in [3,1,4] for j in [9,0,2]   ])
OUTPUT ==
[(4, 9), (4, 0), (4, 2), (2, 9), (2, 0), (2, 2), (4, 9), (4, 0), (4, 2)]
------------------------------------------------------------------------------------------------------
#15.
print(list([(i,j) for i in [2,5,6]] for j in [5,6,8]))
OUTPUT==
[[(2, 5), (5, 5), (6, 5)], [(2, 6), (5, 6), (6, 6)], [(2, 8), (5, 8), (6, 8)]]
------------------------------------------------------------------------------------------------------
#16.Find out the even no and perform cube of that element .

print([(i**3) if i %2==0 else (i**3+1)for i in range(0,10)])
OUTPUT==[0, 2, 8, 28, 64, 126, 216, 344, 512, 730]
------------------------------------------------------------------------------------------------------
#17.Find the string which start with v.
names=["ch","vh","kl","co","lj"]
print([i for i in names if i.startswith("v")])
OUTPUT==['vh']
------------------------------------------------------------------------------------------------------
#18.Find min num and max num from list of list and create dict.

vals= [[1,2,3],[2,3,6],[5,1,9]]
print([{min(i):max(i)} for i in vals])
OUTPUT==[{1: 3}, {2: 6}, {1: 9}]
-------------------------------------------------------------------------------------------------
#19.Create new list using list of list.

vals= [[1,2,3],[2,3,6],[5,1,9]]
print([i for  game in vals for i in game])
OUTPUT==
[1, 2, 3, 2, 3, 6, 5, 1, 9]
---------------------------------------------------------------------------------------------------
#20.Find out the string from list of list which length is greater than 3.

text = [['bar','foo','fooba'],['Rome','Madrid','Houston'], ['aa','bb','cc','dd']]
print([i for j in text for i in j if len(i)>3])
OUTPUT==
['fooba', 'Rome', 'Madrid', 'Houston']
"""



