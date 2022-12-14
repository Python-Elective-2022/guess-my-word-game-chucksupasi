# On this project I have collaborated with the following student: Poon (Class 1102)

def main():
    secret_word = choose_word(word_list)
    print(game_loop(secret_word))

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "word_list.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    print(len(word_list), "words found")
    return word_list

def choose_word(word_list):
    """
    word_list (list): list of words (strings)
    Returns a word from word_list at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable word_list
# so that it can be accessed from anywhere in the program
word_list = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    found_counter = 0
    for letter in secret_word:
        if letter in letters_guessed:
            found_counter += 1
    if found_counter == len(secret_word):
        return True
    else:
        return False
    pass

### Testcases
# print(is_word_guessed('house', ['a', 'e', 'u', 'c', 'r', 'h', 'o', 's']))   Returns: True
# print(is_word_guessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's']))   Returns: False
# print(is_word_guessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))   Returns: True
# print(is_word_guessed('pineapple', []))   Returns: False 

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    output_string = ""
    for letter in secret_word:
        if letter in letters_guessed:
            output_string += letter
        else:
            output_string += "_"
    return output_string
    pass
    
#Testcases
#print(get_guessed_word('apple', ['e', 'i', 'k', 'p', 'r', 's']))   Returns: _pp_e
#print(get_guessed_word('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u']))   Returns: durian
#print(get_guessed_word('sky', ['a', 'e', 's']))   Returns: s__
#print(get_guessed_word('fifty', []))   Returns: _____

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    remaining_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            remaining_letters += letter
    return remaining_letters
    pass

#Testcases 
#print(get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))   Returns: abcdfghjlmnoqtuvwxyz
#print(get_available_letters(['r', 'y', 'd', 'u', 't']))   Returns: abcefghijklmnopqsvwxz
#print(get_available_letters(['r', 'y', 'd', 'u', 't']))  Returns: abcefghijklmnopqsvwxz
#print(get_available_letters([]))   Returns: abcdefghijklmnopqrstuvwxyz

def is_letter_in_word(secret_word, letter_guessed):
    """
    secret_word: string, the word the user is guessing
    letter_guessed: the current letter the user typed in to guess
    returns: boolean, True if the letter_guessed matches at least 1 letter in secret_word;
    False otherwise
    """
    for letter in secret_word:
        if letter == letter_guessed:
            return True
  
def game_loop(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game.
    * At the start of the game, let the user know how many 
      letters the secret_word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses_remaining = 8
    guessed_already = []
    print("Let the game begin!")
    print("I am thinking of a word with", len(secret_word), "letters.")
    print("")
    while guesses_remaining > 0:
        print("You have", guesses_remaining, "guesses remaining.")
        print("Letters available to you: ", get_available_letters(guessed_already))
        current_guess = input("Guess a letter: " ).lower()
        if current_guess in guessed_already:
            print("You fool! You tried this letter already:", get_guessed_word(secret_word, guessed_already))
        else:
            guessed_already.append(current_guess)
            if is_letter_in_word(secret_word, current_guess) == True:
                print("Correct:", get_guessed_word(secret_word, guessed_already))
            else:
                guesses_remaining -= 1
                print("Incorrect, this letter is not in my word:", get_guessed_word(secret_word, guessed_already))
        print("")
        if is_word_guessed(secret_word, guessed_already) == True:
            return "You WIN"
    if is_word_guessed(secret_word, guessed_already) == False:
        return ("GAME OVER ! The word was " + secret_word + ".")
    pass

# Testcases
# you might want to pick your own
# secret_word while you're testing

# print(game_loop("hello"))
# print(game_loop("orange"))
# print(game_loop("blue"))
# print(game_loop("i"))
# print(game_loop("drtihrntir"))
# All secret words above give the correct output when playing the game

if __name__ == "__main__":
    main()