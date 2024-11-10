Chef is playing a mobile game. In the game, Chef's character Chefario can perform special attacks. However, one special attack costs 
X
X mana points to Chefario.

If Chefario currently has 
Y
Y mana points, determine the maximum number of special attacks he can perform.

Input Format
The first line contains a single integer 
T
T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space-separated integers 
X
X and 
Y
Y — the cost of one special attack and the number of mana points Chefario has initially.
Output Format
For each test case, output the maximum number of special attacks Chefario can perform.

Constraints
1
≤
T
≤
1
0
5
1≤T≤10 
5
 
1
≤
X
≤
100
1≤X≤100
1
≤
Y
≤
1000
1≤Y≤1000

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=y//x
    print(z)
