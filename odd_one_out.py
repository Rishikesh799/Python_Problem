##odd one out
 Problem:-
Alice and Bob are getting bored so they decided to play a game.
Alice has n cards having the first n odd numbers written on them. He removes one of the cards at random
and hands the remaining n-1 cards to Bob. Help Bob to find the value of the card Alice has removed.
Input
The first line contains n the numbers of cards Alice has.
The second line contains n-1 space-separated integers representing the values of cards that Bob got.
Output
Print the value of card Alice removed.
Constraints
1≤n≤4000000
Time Limit: 1
Memory Limit: 512
Source Limit:
Explanation
The first 5 odd numbers are 1, 3, 5, 7 and 9 out of which 7 is missing
------------------------------------------------------------------

n=int(input("Enter the no of cards:"))
k=[]
for i in range(1,n+10):
    if i % 2 != 0:
        k.append(i)
import random
no = random.sample(k,10)
k = no.copy()
print(k)

remove1 = input("Alice Do you want to remove element y/n:")
if remove1 == ['y','Y','Yes','YES']:
    pass
z = random.choice(k)
k.pop(no.index(z))

if len(k)!=len(no):

    find_miss = input("Bob do you want to which no is missing?")
    if find_miss == ['y','Y','Yes','YES']:
        pass
    for i in no:
        if i not in k:
            print("missing element is",i)
