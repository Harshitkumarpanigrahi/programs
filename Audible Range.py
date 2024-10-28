Audible Range
Chef's dog binary hears frequencies starting from 
67
67 Hertz to 
45000
45000 Hertz (both inclusive).

If Chef's commands have a frequency of 
X
X Hertz, find whether binary can hear them or not.





t=int(input())
for i in range(t):
    n=int(input())
    if n >= 67 and n <=45000:
        print("YES")
    else:
        print("NO")
