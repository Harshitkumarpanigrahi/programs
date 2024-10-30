
Chef's son wants to go on a roller coaster ride. The height of Chef's son is 
X
X inches while the minimum height required to go on the ride is 
H
H inches. Determine whether he can go on the ride or not.




t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>=y:
        print("YES")
    else:
        print("NO")
    
