from urllib.request import urlopen
import json
from termcolor import colored
 



#extracting only one word from the given link by changing the number parameter and returning a filtered string
def extract_word():
	url =("https://random-word-api.herokuapp.com/word?number=1")
	response = urlopen(url)
	data = response.read().decode("utf-8")
	return data[2:-2]

def instructions():
	print(colored("Welcome to the Hangman game".center(100,' '),'white',attrs=['bold']))
	
	
	print("THE FOLLOWING ARE THE RULES OF THE GAME:")
	print("1.You only get 5 lives to play this game.")
	print("2.Every incorrect guess will result in the deduction 1 life.")
	print("3.For every correct guess you get to play without any deduction in lives.")
	print("4.You win the game if you correctly guess the word without loosing your 5 lives\n")
	
	
	print("INPUT INSTRUCTIONS".center(40,'*'))
	print("1.Kindly enter guesses in the lower case")
	print("2.Any numeric or characterisic input will be taken as a wrong guess, and no lives will be refunded.")
	print("3. Only a single letter input is advised for the guess input.\n")


#Function to check and display if the player has correctly guessed all the words or not 
def game_status(word,guessed):
	flag = False
	for i in word:
		if i in guessed:
			print(i,"",end="")
		else:
			print("_",end="")
			flag = True
	return flag
			


def result(outcome,word):
	if outcome:
		print(colored("Congratualations on winning with the correct guessess!!!\n the word was :",'green',attrs=['bold'])+word+colored(" indeed!!!!!",'green',attrs=['bold']))
	else:
		loose = "Sorry you failed, the word was "
		print(colored(loose,'red',attrs=['bold'])+word)



#Main game function	
def game():
	word = extract_word()
	available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	score = 0 
	lives = 5
	length = len(word)
	correct_guesses = len(set(word))
	guessed = []
	is_word_not_guessed = True
	print("_"*length)
	print("available letters are:\n",*available_letters)
	
	
	#the game will go on until the user either correctly guesses the word or looses all his lives
	while lives > 0 and is_word_not_guessed:
		guess = input("\nEnter the alphabet you want to guess: ")
		
		#if and else block for updating the score and lives, while adding the letters guessed by the player
		if guess in word:
			print(colored("you guessed it right!","green",attrs=['bold']))
			if guess in guessed:
				pass
			else:
				score +=1
				guessed.append(guess)
		else:
			lives = lives - 1
			print(colored("Wrong guess!!!","red",attrs=['bold']))
			
		
		#removing letters used by the player to give him a better clarity of his options	       
		if guess in available_letters:
			available_letters.remove(guess)
		
		#Calling the function to see if the player has guessed the word or not and print the progress of the player in the game	
		is_word_not_guessed = game_status(word,guessed)
		
		#Stats of the player after every guess
		print("\navailable letters are:\n",*available_letters)
		life = "no of lives left:"+str(lives)+"\n\n"
		print(colored(life,'white',attrs=["bold"]))
		
	#Calling the results function to display the game outcome messages	
	if score == correct_guesses:
		result(True,word)
	else:
		result(False,word)
	
	
	
while True:
	name = input("\nEnter your name:")
	print("Hi ",name)
	instructions()
	game()
	status = input("\nDo you still want to play?\n If you want to enter y/Y\n or press any key if you want to quit the game\ninput : ")
	if status in ['y','Y']:
		print("All the best")
	else:
		print("Thank you!!!!")
		break
