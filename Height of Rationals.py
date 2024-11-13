In a recent breakthrough in mathematics, the proof utilized a concept called Height.

Consider a fraction 
a
b
b
a
​
 . Its Height is defined as the maximum of its numerator and denominator. So, for example, the Height of 
3
19
19
3
​
  would be 
19
19, and the Height of 
27
4
4
27
​
  would be 
27
27.

Given 
a
a and 
b
b, find the Height of 
a
b
b
a
​
 .

Input Format
The only line of input contains two integers, 
a
a and 
b
b.

Output Format
Output a single integer, which is the Height of 
a
b
b
a
​
 .

Constraints
1
≤
a
,
b
≤
100
1≤a,b≤100
a
a and 
b
b do not have any common factors.

x,y=map(int,input().split())
print(max(x,y))
