Bone Appetit
Trick or treat, bags of sweets, ghosts are walking down the street

It's Halloween and Suri Bhai is out to get his treats.
There are two sectors in his neighborhood, "Bones" and "Blood". They have 
N
N and 
M
M people, respectively.

Each person in "Bones" will hand out 
X
X treats, and each person in "Blood" will hand out 
Y
Y treats.
How many treats does Suri Bhai get from visiting everyone in his neighborhood in total?


x,y=map(int,input().split())
n,m=map(int,input().split())
res=(n*x)+(m*y)
print(res)
