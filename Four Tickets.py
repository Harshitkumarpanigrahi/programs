
Four friends want to attend a concert. Each ticket costs 
X
X rupees.
They have decided to go to the concert if and only if the total cost of the tickets does not exceed 
1000
1000 rupees.

Determine whether they will be going to the concert or not.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single integer 
X
X, the cost of each ticket.
Output Format
For each test case, output YES if they will be going to the concert, NO otherwise.

You can print each character in uppercase or lowercase. For example, the strings YES, yes, Yes, and yES, are all considered identical.

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
≤
1000
1≤X≤1000




t=int(input())
for i in range(t):
    n=int(input())
    if n*4<=1000:
        print("YES")
    else:
        print("NO")
