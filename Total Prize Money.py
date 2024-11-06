
In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:

Top 
10
10 participants receive rupees 
X
X each.
Participants with rank 
11
11 to 
100
100 (both inclusive) receive rupees 
Y
Y each.
Find the total prize money over all the contestants.

Input Format
First line will contain 
T
T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers 
X
X and 
Y
Y - the prize for top 
10
10 rankers and the prize for ranks 
11
11 to 
100
100 respectively.
Output Format
For each test case, output the total prize money over all the contestants.

Constraints
1
≤
T
≤
1000
1≤T≤1000
1
≤
Y
≤
X
≤
1000
1≤Y≤X≤1000





t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    res=(10*x)+(90*y)
    print(res)
    
