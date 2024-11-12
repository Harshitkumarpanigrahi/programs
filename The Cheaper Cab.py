Chef has to travel to another place. For this, he can avail any one of two cab services.

The first cab service charges 
X
X rupees.
The second cab service charges 
Y
Y rupees.
Chef wants to spend the minimum amount of money. Which cab service should Chef take?

Input Format
The first line will contain 
T
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers 
X
X and 
Y
Y - the prices of first and second cab services respectively.
Output Format
For each test case, output FIRST if the first cab service is cheaper, output SECOND if the second cab service is cheaper, output ANY if both cab services have the same price.

You may print each character of FIRST, SECOND and ANY in uppercase or lowercase (for example, any, aNy, Any will be considered identical).

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
        print('FIRST')
    elif x==y:
        print('ANY')
    else:
        print('SECOND')
