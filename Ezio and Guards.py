Ezio can manipulate at most 
X
X number of guards with the apple of eden.

Given that there are 
Y
Y number of guards, predict if he can safely manipulate all of them.

Input Format
First line will contain 
T
T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers 
X
X and 
Y
Y.
Output Format
For each test case, print 
YES
YES if it is possible for Ezio to manipulate all the guards. Otherwise, print 
NO
NO.

You may print each character of the string in uppercase or lowercase (for example, the strings 
YeS
YeS, 
yEs
yEs, 
yes
yes and 
YES
YES will all be treated as identical).

Constraints
1
≤
T
≤
100
1≤T≤100
1
≤
X
,
Y
≤
100
1≤X,Y≤100

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<y:
        print('no')
    else:
        print('yes')
