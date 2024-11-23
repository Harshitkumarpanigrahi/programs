Chef bought car insurance. The policy of the insurance is:

The maximum rebatable amount for any damage is Rs 
X
X lakhs.
If the amount required for repairing the damage is 
≤
X
≤X lakhs, that amount is rebated in full.
Chef's car meets an accident and required Rs 
Y
Y lakhs for repairing.

Determine the amount that will be rebated by the insurance company.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case contains two space-separated integers 
X
X and 
Y
Y.
Output Format
For each test case, output the amount (in lakhs) that will be rebated by the insurance company.

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
≤
30
1≤X,Y≤30

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        print(y)
    else:
        print(x)
        
