import random
num = random.randint(0,101)
i=0
while(True):
  try:
    guess = int(input("Guess the number between 0 to 100: "))
    if(0<=num<=100):
      if(num>guess):
        print("The number is greater than your guess")
      elif(num<guess):
        print("The number is less than your guess")
      else:
        print("You guessed the number")
        break
      if (int(input("Enter 0 to quit or 1 to continue \n"))==0):
        print(f"The number was {num}")
        break
      i+=1
    else:
      print("Enter number in range 0 to 100")
  except(ValueError):
    print("Invalid input! Please enter a Whole number between 0 and 100")
print(f"You took {i+1} guesses")