import random
print("your have only 7 changes to win this game")
choice=int(input("enter the number:"))
while choice>100:
    print("your number is greater than 100")
    choice=int(input("enter the number again:"))
random_number = random.randint(1, 100)
chances=[]
for i in range(1,8):
        if random_number != choice:
            chances.append(i)
            print(f"this is {i} chance ")
            if i==7:
                print("the ans is", random_number)
                print(exit("game over"))
        if random_number>choice:
            print("your choice is less than random number")
            choice=int(input("enter the number:"))
        elif random_number<choice:
            print("your choice is greater than random number")
            choice=int(input("enter the number:"))
        else:
            print(exit("YOU WON THIS GAME"))

print("You won this game")

