
DAIICT college students want to attend an IPL match.

A total of 
N
N students from the college want to go while only 
M
M tickets are available for the match.

Determine how many students won't be able to book tickets.



t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<y:
        print("0")
    else:
        print(x-y)
