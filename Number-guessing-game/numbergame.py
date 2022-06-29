import random
import math
# taking input from user
lower=int(input("Enter the lower bound-"))
upper=int(input("Enter the upper bound-"))
# generating random number between
# the lower and upper
x=random.randint(lower,upper)
#print(x)
print(round(math.log(upper-lower+1,2)))
count=0
while count<=(math.log(upper-lower+1,2)):
    count=count+1
    guess = int(input("Guess a number:- "))
    if guess==x:
        print("Congratulations you did it in ",
              count, " try")
        break
    if guess>x:
        print("your value is high")
    if guess<x:
        print("your value is small")
if count>(math.log(upper-lower+1,2)):
    print("The number is\n",x)
    print("Better luck next time")