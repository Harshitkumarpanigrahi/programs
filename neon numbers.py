n=int(input())
sqr=n*n
sum=0
while sqr>0:
    dig=sqr%10
    sum=sum+dig
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number") 
