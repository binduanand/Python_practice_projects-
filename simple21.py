import random

class CustomError(Exception):
  pass
  
num = [0]
print("Welcome to 21 Number Game \n You Start")

while True:
  try:
    n = int(input("Do you want to enter 1,2 or 3 numbers? "))
    if n<1 or n>3:
      raise CustomError
    
    for i in range(n):
      num.append(num[-1]+1)
      if num[-1] == 21:
        print("You lose")
        exit()
    print(num)
  
    comp = random.choice([1,2,3])
    for i in range(comp):
      num.append(num[-1]+1)
      if num[-1] >= 21:
        print("You Won!!!")
        exit()
    print(f"Computer added {num}\n")
  except ValueError:
    print("Wrong Input! ")
  except CustomError:
    print("enter 1,2 or 3 only")
