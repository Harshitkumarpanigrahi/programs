Chef is watching TV. The current volume of the TV is 
X
X. Pressing the volume up button of the TV remote increases the volume by 
1
1 while pressing the volume down button decreases the volume by 
1
1. Chef wants to change the volume from 
X
X to 
Y
Y. Find the minimum number of button presses required to do so.

Input Format
The first line contains a single integer 
T
T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains two integers 
X
X and 
Y
Y - the initial volume and final volume of the TV.
Output Format
For each test case, output the minimum number of times Chef has to press a button to change the volume from 
X
X to 
Y
Y.

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
,
Y
≤
100
1≤X,Y≤100


t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print(x-y)
    else:
        print(y-x)
