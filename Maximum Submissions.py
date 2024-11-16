A participant can make 
1
1 submission every 
30
30 seconds. If a contest lasts for 
X
X minutes, what is the maximum number of submissions that the participant can make during it?

It is also given that the participant cannot make any submission in the last 
5
5 seconds of the contest.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single integer 
X
X, denoting the number of minutes.
Output Format
For each test case, output the maximum number of submissions a participant can make in 
X
X minutes.

Constraints
1
≤
T
≤
30
1≤T≤30
1
≤
X
≤
30
1≤X≤30


t=int(input())
for i in range(t):
    x=int(input())
    res=x*2
    print(res)
