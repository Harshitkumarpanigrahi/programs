
In Chefland, a football player gets 
2
2 points for each goal and 
1
1 point for each assist.

Messi has 
A
A goals and 
B
B assists this season, whereas Ronaldo has 
X
X goals and 
Y
Y assists.
Find out the player with more points this season.

Input Format
The first and only line of input will contains four space-separated integers 
A
A, 
B
B, 
X
X and 
Y
Y, the number of goals and assists that Messi has and the number of goals and assists that Ronaldo has, respectively.
Output Format
Print a single line containing:

Messi, if Messi has more points than Ronaldo.
Ronaldo, if Ronaldo has more points than Messi.
Equal, if both have equal points.
You can print each character in uppercase or lowercase. For example, the strings Messi, MESSI, messi, and MeSSi are considered identical.

Constraints
0
≤
A
,
B
,
X
,
Y
≤
100
0≤A,B,X,Y≤100



a,b,x,y=map(int,input().split())
z=(a*2)+(b*1)
s=(x*2)+(y*1)
if z>s:
    print("Messi")
elif s>z:
    print("Ronaldo")
else:
    print("Equal")
