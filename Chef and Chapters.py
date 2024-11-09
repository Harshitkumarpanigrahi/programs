This semester, Chef took 
X
X courses. Each course has 
Y
Y units and each unit has 
Z
Z chapters in it.

Find the total number of chapters Chef has to study this semester.

Input Format
The first line will contain 
T
T, the number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three space-separated integers 
X
,
Y
,
X,Y, and 
Z
Z.
Output Format
For each test case, output in a single line the total number of chapters Chef has to study this semester.

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
,
Y
,
Z
≤
1000
1≤X,Y,Z≤1000


t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    res=x*y*z
    print(res)
    
