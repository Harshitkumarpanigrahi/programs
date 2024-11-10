Chef organised a 
30
30 kilometres marathon in Chefland.
The participants receive medals on completing the marathon as following:

If the total time taken is less than 
3
3 hours, they receive a GOLD medal.
If the total time taken is greater than equal to 
3
3 hours but less than 
6
6 hours, they receive a SILVER medal.
If the total time taken is greater than equal to 
6
6 hours, they receive a BRONZE medal.
Chefina participated in the marathon and completed it in 
X
X hours. Which medal would she receive?

Input Format
The input consists of a single integer 
X
X — the number of hours Chefina took to complete the marathon.
Output Format
Output the medal Chefina would recieve.

Note that you may print each character in uppercase or lowercase. For example, the strings GOLD, gold, Gold, and gOlD are considered the same.

Constraints
1
≤
X
≤
10
1≤X≤10.



x=int(input())
if x<3:
    print("GOLD")
elif x>=3 and x<6:
    print("SILVER")
else:
    print("BRONZE")
