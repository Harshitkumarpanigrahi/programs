Fill the Bucket
Chef has a bucket having a capacity of 
K
K liters. It is already filled with 
X
X liters of water.

Find the maximum amount of extra water in liters that Chef can fill in the bucket without overflowing.

Input Format
The first line will contain 
T
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space separated integers 
K
K and 
X
X - as mentioned in the problem.
Output Format
For each test case, output in a single line, the amount of extra water in liters that Chef can fill in the bucket without overflowing.

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
K
≤
1000
1≤X<K≤1000

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print(x-y)
