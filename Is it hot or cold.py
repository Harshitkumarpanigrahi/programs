
Chef considers the climate HOT if the temperature is above 
20
20, otherwise he considers it COLD. You are given the temperature 
C
C, find whether the climate is HOT or COLD.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
The first and only line of each test case contains a single integer, the temperature 
C
C.
Output Format
For each test case, print on a new line whether the climate is HOT or COLD.

You may print each character of the string in either uppercase or lowercase (for example, the strings hOt, hot, Hot, and HOT will all be treated as identical).

Constraints
1
≤
T
≤
50
1≤T≤50
0
≤
C
≤
40
0≤C≤40

t=int(input())
for i in range(t):
    c=int(input())
    if c>20:
        print('hot')
    else:
        print('cold')
