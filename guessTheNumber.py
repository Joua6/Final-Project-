'''
Created on May 9, 2020

@author: ITAUser
'''
#OBJECTIVE:
#player guess a number from 1 to 25
#loop the whole game, so that have five guess
#add statement to welcome player and teach the rules 
#create code that takes players input 
#create code that tell if guess is too high or to low 
#use import random 


#PSEUDOCODE:
#import random 
import random 

#print Welcome to the Number guessing game
print("Welcome to the Number guessing game") 
  
# randint function to generate the random number from 1 to 9 
number = random.randint(1, 25) 
  
# Set players chances to 0
chances = 0
  
print("Guess a number (between 1 and 25):")  
print ("You have five chances to guess.")

# While loop to count the number of chances 
while chances < 5: 
      
#print type any number from 1 to 25.
# crate code for players to guess a number between 1 to 25
    print ("Type any number from 1 to 25.")
    guess = int(input()) 
# Crate code that compare the players guess to the number  
# if number entered by the player is same break and print you won  
 
    if guess == number:  
        print("Congratulation YOU WON!!!") 
        break
          
# if the number is smaller than print Your guess was too low, Guess a number higher
    elif guess < number: 
        print("Your guess was too low: Guess a number higher") 
  
# The user entered number is greater than print Your guess was too high: Guess a number lower               
    else: 
        print("Your guess was too high: Guess a number lower") 
          
    # Increase the value of chance by 1 
    chances += 1
# Check the amount of chances used. If chances is greater than five print you lose. Tell the player the number 
if chances > 5: 
    print("YOU LOSE!!! The number is", number) 
