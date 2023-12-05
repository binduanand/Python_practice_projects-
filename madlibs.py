class Madlib:
  def __init__(self, ad, verb, noun, color, animal, action):
    print(f"On a {ad} afternoon, I decided to {verb} to the {noun}. Along the way, I was encountered by a {color}ed {animal} who was {action}.")

  


ad = input("Enter an adjective: ")
verb = input("Enter a verb: ")
noun = input("Enter a noun: ")
color = input("Enter a color: ")
animal = input("Enter an animal: ")
action = input("Enter an action: ")
user = Madlib(ad,verb,noun,color,animal,action)