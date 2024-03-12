import random
n=random.randint(1,20)
flag=False
while flag!=True:
    guess=int(input("Guess your number:"))
    if(guess==n):
        print("You Won")
        flag=True
    else:
        print("You Lost")
