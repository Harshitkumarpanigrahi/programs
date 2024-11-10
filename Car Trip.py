Chef rented a car for a day.

Usually, the cost of the car is Rs 
10
10 per km. However, since Chef has booked the car for the whole day, he needs to pay for at least 
300
300 kms even if the car runs less than 
300
300 kms.

If the car ran 
X
X kms, determine the cost Chef needs to pay.

Input Format
The first line of input will contain a single integer 
T
T, denoting the number of test cases.
Each test case consists of a single integer 
X
X - denoting the number of kms Chef travelled.
Output Format
For each test case, output the cost Chef needs to pay.

Constraints
1
≤
T
≤
100
1≤T≤100
1
≤
X
≤
1000
1≤X≤1000

t=int(input())
for i in range(t):
    x=int(input())
    if x<=300:
        print(300*10)
    else:
        print(x*10)
