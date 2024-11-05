
Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.

Given that Chef bought the stock at value 
X
X and sold it at value 
Y
Y. Help him calculate whether he made a profit, loss, or was it a neutral deal.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single line of input containing two space-separated integers 
X
X and 
Y
Y, denoting the value at which Chef bought and sold the stock respectively.
Output Format
For each test case, output PROFIT if Chef made a profit on the deal, LOSS if Chef incurred a loss on the deal, and NEUTRAL otherwise.

The checker is case-insensitive so answers like pROfiT, profit, and PROFIT would be considered the same.






t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x>y:
        print("LOSS")
    elif x==y:
        print("NEUTRAL")
    elif x<y:
        print("PROFIT")
    else:
        print("LOSS")
