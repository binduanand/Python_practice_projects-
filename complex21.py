import random

class CustomError(Exception):
    pass

num = [0]
print("Welcome to 21 Number Game \n You Start")

while True:
    n = int(input("Would you like to enter 1, 2 or 3 numbers? "))
    while n > 0:
        try:
            user = int(input("Enter number: "))
            if num[-1] != user - 1:
                raise CustomError
            num.append(user)
            n -= 1
        except ValueError:
            print("Enter integers only")
        except CustomError:
            print("Wrong input")

        if num[-1] == 21:
            print("You lose")
            print(num)
            exit()

    print(num, "\n")

    n = random.choice([1, 2, 3])
    for i in range(n):
        num.append(num[-1] + 1)
        if num[-1] == 21:
            print("Computer added: ", num)
            print("You lose")
            print(num)
            exit()
