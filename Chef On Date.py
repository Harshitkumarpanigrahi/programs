
Chef and his girlfriend went on a date. Chef took 
X
X dollars with him, and was quite sure that this would be enough to pay the bill. At the end, the waiter brought a bill of 
Y
Y dollars. Print "YES" if Chef has enough money to pay the bill, or "NO" if he has to borrow from his girlfriend and leave a bad impression on her.



t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<y:
        print("NO")
    else:
        print("YES")
