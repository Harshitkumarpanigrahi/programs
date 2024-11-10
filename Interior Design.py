Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.

For the first style, tiling the floor will cost 
X
1
X 
1
​
  rupees and painting the walls will cost 
Y
1
Y 
1
​
  rupees.

For the second style, tiling the floor will cost 
X
2
X 
2
​
  rupees and painting the walls will cost 
Y
2
Y 
2
​
  rupees.

Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior design?

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single line of input, containing 
4
4 space-separated integers 
X
1
,
Y
1
,
X
2
,
Y
2
X 
1
​
 ,Y 
1
​
 ,X 
2
​
 ,Y 
2
​
  as described in the statement.
Output Format
For each test case, output on a new line the amount Chef will pay for interior design.

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
1
,
Y
1
,
X
2
,
Y
2
≤
100
1≤X 
1
​
 ,Y 
1
​
 ,X 
2
​
 ,Y 
2
​
 ≤100



t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    m=a+b
    n=c+d
    if m<n:
        print(m)
    else:
        print(n)
    
