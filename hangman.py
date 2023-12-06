import random

characters = ["HarryPotter","HermioneGranger","RonWeasley","DracoMalfoy", "SeverusSnape", "LunaLovegood","NevilleLongbottom", "GinnyWeasley", "Dobby","Voldemort","AlbusDumbledore","SiriusBlack","RemusLupin","Hagrid"]

word = random.choice(characters).upper() 
print("WELCOME TO HANGMAN (Harry Potter Edition)")
print("Note: There is no space between first and last name")
guesses = ''
choice = 3
while choice > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else: 
            print('_', end="")
            failed += 1
    if failed == 0:
        print("\nYou won")
        break  
    guess = input("\nEnter a character: ").upper()
    guesses += guess
    if guess not in word:
        choice -= 1
        print(f"Wrong choices left: {choice}")

    if choice == 0:
        print(f"GAME OVER. The correct word was: {word}")
        break  



    


