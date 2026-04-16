#Name: Robert Christain Horne
#Date: September 15 2025
#Filename: GuessingGame - 1 Player.py

#Imports Python's random module.
import random

#Intitalizing the variables.
comNumber = 0
playerGuess = 0
guess_counter = 0


#Intro flavor text
#"\n is used for new line. Simliar to coding in C."
print("Welcome to the number guessing game.")
print("The objective to this game is to guess the number the computer will enter.\n")

#Sets a random number between 1 and 100.
comNumber = random.randint(1, 100)

#Loop will continue to occur as long as the guess number does not equal the compters's random number.
while playerGuess != comNumber:
        
        #Increments the guess counter and displays it to the Player.
        guess_counter = guess_counter + 1
        print(f"This is guess number {guess_counter}.\n")
        
        #Player will input their guess.
        playerGuess = int(input("Enter your guess: "))

        #Checks if the number is between 1 and 100.
        if playerGuess >= 1 and playerGuess <= 100:
            #If true, the game will check to see if the number is too high or too low.
            if playerGuess > comNumber:
                print("Your guess was too high.\n")
            elif playerGuess < comNumber:
                print("Your guess was too low.\n")
        else:
            #If false, the game will ask the player to input another number. This will count as a guess.
            print("Invaild number. Your guess must be between 1 and 100.\n")
        
#If the player succeeds, the game will display both Computer's number and the amount of guess it took.  
print("")  
print(f"----Congratulations! The correct number was {comNumber}!----")
print(f"----You guessed the correct number in {guess_counter} guesses!----\n")


#Keeps the program from immediately shutting down upon finishing.
input("Press Enter to exit.")