#EXERCISES BOOST PROGRAM 

#1 - #ROCK, PAPER AND SICSSORS: Create a program that simulates a “Rock, Paper, Scissors” game between the user and the computer.

# Requirements:
# 1. Get the user's input (choose an object: rock, paper, or scissors)
# 2. Randomly select an object for the computer
# 3. Print the object that was randomly chosen by the computer
# 4. Compare the user's choice with the computer's choice
# 5. Show who wins
# 6. Ask if user wants to play again (yes/no):. lower()
# 7. If 'play again' isn't yes, print "thanks for playing"

#Start
#Starting the randomly choice of objects 
import random
options = ['rock', 'paper', 'sicssors']

#start
while True:
    object_user = input('chose rock, paper or sicssors: '). lower() #coletando a escolha do usuário
    object_random = random.choice(options) #coletando a escolha aleatória do computador
    print(f'You chose {object_user} and I chose { object_random}.') 

    if object_user ==  object_random:
        print('Its a tie!')
    elif (object_user == 'rock' and  object_random == 'paper') or (object_user == 'paper' and    object_random == 'rock') or (object_user == 'sicssors' and  object_random == 'paper'):
        print('You win!')
    else:
        print('You lose')
    play_again = input('Would you like to play again? (yes/no): '). lower()
    if play_again != 'yes':
        print('Thanks for playing')
        break
#Finish