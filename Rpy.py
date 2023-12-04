import random
comp = random.choice(["rock","paper","scissors"])

user = input("Rock, paper, or scissors? ")
print(f"You chose:{user}")
if user.lower() not in ["rock","paper","scissors"]:
  print("Invalid Input")
else:
  if comp==user:
     print(f"Tie, Both chose:{comp}")
  elif ((comp=="rock" and user=="scissors") or 
        (comp=="paper" and user=="rock") or 
        (comp=="scissors" and user=="paper")):
      print(f"You lose, Computer chose:{comp}")
  else:
      print(f"You win, Computer chose:{comp}")
  

  