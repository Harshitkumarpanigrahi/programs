Alice buys a toy with a selling price of 
100
100 rupees. There is a discount of 
x
x percent on the toy. Find the amount Alice needs to pay for it.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case contains a single integer, 
x
x — the discount on the toy.
Output Format
For each test case, output on a new line the price that Alice needs to pay.

Constraints
1
≤
T
≤
100
1≤T≤100
0
≤
x
<
100
0≤x<100

t=int(input())
for i in range(t):
    x=int(input())
    res=100-x
    print(res)
