Chef categorises an instagram account as spam, if, the following count of the account is more than 
10
10 times the count of followers.

Given the following and follower count of an account as 
X
X and 
Y
Y respectively, find whether it is a spam account.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two space-separated integers 
X
X and 
Y
Y — the following and follower count of an account, respectively.
Output Format
For each test case, output on a new line, YES, if the account is spam and NO otherwise.

You may print each character of the string in uppercase or lowercase. For example, the strings YES, yes, Yes and yES are identical.

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
    if x>10*y:
        print('yes')
    else:
        print('no')
