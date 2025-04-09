#Guess the number human
import random 

def computer_guesses_number():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    feedback = '' #This variable will store your response to each guess (whether it's too high, too low, or correct). It starts empty.
    attempts = 0

    while feedback != 'c': #This loop runs as long as your feedback is not 'c' (which stands for correct). Once the computer guesses right, the loop stops.
          guess = random.randint(low,high) #The computer randomly picks a number between the current low and high values
          attempts += 1
          feedback = input(f'is {guess} too high (H), too low (L) or correct (C)?') #Asks you to give feedback on the computer’s guess
          if feedback == 'H':
               high = guess - 1 #If the guess was too high, then the highest possible correct answer is below the guess—so the high value is updated
          elif feedback == 'L':
               low = guess + 1 
          else: 
            print(f'Yay! The computer guessed your number, {guess}, in {attempts} attempts')
            break    

# Run the game
computer_guesses_number()
