"""--------------------------FUNCTION EXAMPLE-----------------------------------------------
#1.write function that inputs a number and prints the multiplication table of that number.
def table(x):
    for i in range(1,11):
        print(x,"*",i,"=",x*i)
n=int(input("Enter the digit you want a table :"))
table(n)
----------------------------------------------------------------------------------------
# 2.Write program to to print twins primes less than 1000.If two consecutive odd num are both prime then they  are known as prime.
def prime(a):
    co=0
    if a>1:
        for i in range(1,a+1):
            if a%i==0:
                co=co+1
        if co == 2:
            return True
        else:
            return False
def checkcon(x):
    for j in range(x):
        if (prime(j) == True) and (prime(j+2)==True):
            print((j,j+2),end=" ")
        else:
            pass
(checkcon(100))
-----------------------------------------------------------------------------------------------------
#3.Write program to find out the prime factors of numbers.
def Pfact(x):
    s=[]
    i=2
    while i <= x:
         if x % i == 0:
             s.append(i)
             x = x // i
         else:
             i = i+1
    print(s)
n = int(input("enter the no:"))
Pfact(n)
-----------------------------------------------------------------------------------------------
#4.write function convert decimal into binary
def num(x):
    d=[]
    i=2              ## if we want covert into octal i=8 and into hexadecimal i=16
    if x > 1:
        while i<=x:
            y = x % i
            d.append(y)
            x = x//i
        else:
            d.append(x)
    print("".join(map(str,d[::-1])))
n = int (input ("enter the no which convert into decimal to binary:") )
num(n)
------------------------------------------------------------------------------------------------
#5.Write a program check whether its armstrong or not.
def arm(x):
    e=x
    s=0
    while x>0:
        i=x%10
        s=s+i*i*i
        x=x//10
    if e == s:
        return "Its armstrong num"
    else:
        return "Not armstrong"
n = int(input("enter the no:"))
print(arm(n))
----------------------------------------------------------------------------------------------------
#6.Write function of product digit that inputs a number and return the product of that digits of number.
def proDuct(x):
    s=1
    while x>0:
        i=x%10
        s=s*i
        x=x//10
    print(s)
n = int(input("Enter the no:"))
proDuct(n)
------------------------------------------------------------------------------------------------

#7.write program of getting MDR.
def mdr(x):
    y=[0,1,2,3,4,5,6,7,8,9]
    s=1
    if x in y:
        return x
    else:
        while x>0:
            i=x%10
            s=s*i
            x=x//10

    return mdr(s)
print(mdr(86))
print(mdr(341))
----------------------------------------------------------------------------------------------------------
#8.Write the function of sum of prper divisors number.proper divisors num means those num by which yhe num is divisible.
# Except num itself
def sumP(x):
    d=[]
    for i in range(1,x):
        if x % i ==0:
            d.append(i)
    print(d)
    print(sum(d))
n = int(input("Enter the no:"))
sumP(n)
-------------------------------------------------------------------------------------------------------
#9.Write the fuction of perfect numbers.perfect num means if the sum of proper divisors num is equal to yhe number.
def sum(x):
    s=0
    for i in range(1,x):
        if x % i ==0:
            s=s+i
    if x == s:
        return True
    else:
        return False
def check(k):
    for a in range(2,k):
        if sum(a)==True:
            print(a,end=" ")
        else:
            pass
n = int(input("Enter the no:"))
check(n)
-------------------------------------------------------------------------------------------------------
#11.Write program which can filter odd numbers in alist by using filteration.
print(list(filter(lambda x:x%2!=0,range(1,101))))
----------------------------------------------------------------------------------------------------------
#12.Write program which can map() to make list whose elements are cube of elements in given list.
print(list(map(lambda x:x**3,range(1,11))))
-------------------------------------------------------------------------------------------------------------
#13.Write programwhich can make map(),and filter to make a list whose elements are cubeof even numbers in agiven list.
y=list(filter(lambda x:x%2==0,range(1,50)))
print(list(map(lambda x:x**3,y)))
"""

















