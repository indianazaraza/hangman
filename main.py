import random
import re

with open("words.txt", "r") as file:
	#read the file with the list of words
	words_list:list = file.readlines()
	#choose a word
	secret_word:str = words_list[random.randint(0, 224)]

hyphenated_word:list = []

#fill the list with hyphens the same length as the secret word
#minus one is because the secret word adds an extra character, a whitespace
for letter in secret_word[:-1]:
	hyphenated_word.append('-')

def get_results(secret_word) -> None:
	"""reports game results, if the user lost, the given secret word is displayed on the screen
	
	:param secret_word: word to guess
	
	:type secret_word: str
	"""
	answer:str = input("Write the word or press enter: ")

	if answer == secret_word[:-1]:
		print("\n¡Win!")
	else:
		print(f"\nLost\nThe word was {secret_word}")

def find_matches(hyphenated_word, secret_word) -> None:
	"""
	find matches of the secret word in the hyphenated word
	
	:param 
	hyphenated_word: hidden word
	secret_word: word to guess
	
	:type both str
	"""
	letter:str = input("Letter: ")
		
	try:
		#returns all the indices where the letter entered by the user is found
		indexes:list = [i.start() for i in re.finditer(letter, secret_word)]	 

		#fills the hyphened word with the letter entered by the user in the positions where there were matches
		for index in indexes:
			hyphenated_word[index] = letter

		print("".join(hyphenated_word), "\n")
	except IndexError:
		print("I need a letter")

def play() -> None:
	"""initialize the game process
	"""
	attempts:int = 5
	
	print(f"The word has {len(hyphenated_word)} letters\nYou have 5 attempts\n")
	
	while attempts > 0:
		attempts-=1

		print("================== Try n°", attempts+1, "==============\n")
		
		find_matches(hyphenated_word, secret_word)
		
		answer:str = input("Do you know the word?: y/n ")
			
		if answer == 'y':
			break

	get_results(secret_word)

if __name__ == "__main__":
	play() 