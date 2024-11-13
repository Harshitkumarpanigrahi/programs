Chef recently started selling a special fruit.
He has been selling the fruit for 
X
X rupees (
X
X is a multiple of 
100
100). He earns a profit of 
Y
Y rupees on selling the fruit currently.

Chef decided to increase the selling price by 
10
%
10%. Please help him calculate his new profit after the increase in selling price.

Note that only the selling price has been increased and the buying price is same.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single line of input containing two space-separated integers 
X
X and 
Y
Y denoting the initial selling price and the profit respectively.
Output Format
For each test case, output a single integer, denoting the new profit.

Constraints
1
≤
T
≤
1000
1≤T≤1000
1
≤
X
≤
1000
1≤X≤1000
1
≤
Y
≤
100
1≤Y≤100
X
X is a multiple of 
100
100.


t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    z=x-y #90
    per=(x//100)*10+x     #100/10
    res=per-z
    print(res)
        
