In a certain month, Chef earned 
X
X rupees while Chefina earned 
Y
Y rupees such that 
Y
>
X
Y>X.
Since they want to end up with exactly the same amount, they decide to donate the difference between their income to a charity.

Find the amount they donate in the month.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of two space-separated integers 
X
X and 
Y
Y — the income of Chef and Chefina in a month, respectively.
Output Format
For each test case, output on a new line, the amount they donate in the month.

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
<
Y
≤
10
1≤X<Y≤10




t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    res=y-x
    print(res)
