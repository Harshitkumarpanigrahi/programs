To access CRED programs, one needs to have a credit score of 
750
750 or more.
Given that the present credit score is 
X
X, determine if one can access CRED programs or not.

If it is possible to access CRED programs, output 
YES
YES, otherwise output 
NO
NO.

Input Format
The first and only line of input contains a single integer 
X
X, the credit score.

Output Format
Print 
YES
YES if it is possible to access CRED programs. Otherwise, print 
NO
NO.

You may print each character of the string in uppercase or lowercase (for example, the strings 
YeS
YeS, 
yEs
yEs, 
yes
yes and 
YES
YES will all be treated as identical).

Constraints
0
≤
X
≤
1000
0≤X≤1000


x=int(input())
if x>=750:
    print('yes')
else:
    print('no')
