There are 
N
N bikes and 
M
M cars on the road.

Each bike has 
2
2 tyres.
Each car has 
4
4 tyres.
Find the total number of tyres on the road.

Input Format
The first line will contain 
T
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers 
N
,
M
N,M.
Output Format
For each test case, output in a single line, the total number of tyres on the road.

Constraints
1
≤
T
≤
1000
1≤T≤1000
0
≤
N
,
M
≤
100
0≤N,M≤100

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    b=x*2
    c=y*4
    print(b+c)
    
