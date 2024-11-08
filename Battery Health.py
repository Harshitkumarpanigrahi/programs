
Apple considers any iPhone with a battery health of 
80
%
80% or above, to be in optimal condition.

Given that your iPhone has 
X
%
X% battery health, find whether it is in optimal condition.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case contains an integer 
X
X — the battery health.
Output Format
For each test case, output on a new line, YES, if the battery is in optimal condition, and NO otherwise.

You may print each character in uppercase or lowercase. For example, NO, no, No and nO, are all considered identical.

Constraints
1
≤
T
≤
100
1≤T≤100
0
≤
X
≤
100
0≤X≤100



t=int(input())
for i in range(t):
    n=int(input())
    if n>=80:
        print("YES")
    else:
        print("NO")
