import random

def load_words():
    '''
    parameters: none
    returns: list, of words the program used for the game.
    '''
    print("Loading word list from file...")
    inFile = open("d:\\Coding\\Python-Practice\\hangman\\words.txt", 'r')  # Unfortunately inFile = open('words.txt', 'r') doesn't work at all. Please change directory before use!!
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.\n")
    return wordlist


wordlist = load_words()


def choose_word(wordlist):
    '''
    wordlist: list, of words the program used for the game.
    returns: string, random choice from the wordlist
    '''
    return random.choice(wordlist)


missedLetters = []   # list (of letters), which have not benn guessed so far
letters_guessed = []  # list (of letters), which letters have been guessed so far
secret_word = choose_word(wordlist).lower()  # string, the word the user is guessing
attempts = 6  # int, the amount of attempts at the start of each game.
warnings = 3  # int, the amount of warnings


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    found_all_letters = True
    for letter in secret_word:
      if letter in letters_guessed:
        continue
      else:
        found_all_letters = False
    return found_all_letters


  

def get_guessed_word(letters_guessed, missed_letters) :
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    missedLetters: list (of letters), which have not benn guessed so far
    returns: string, the letter the user entered.
    '''

    global warnings
    correct_input = False
    while True:
        print('Please guess a letter: ')
        guess = input()
        guess.lower()
        if (guess in letters_guessed) or (guess in missed_letters):
            return guess, correct_input
        else:
            if len(guess) == 1:
                if guess in "abcdefghijklmnopqrstuvwxyz":
                    correct_input = False
                    return guess, correct_input
            else:
                if guess == "":
                    correct_input = False
                    return guess, correct_input
                else:
                    correct_input = False
                    return guess, correct_input
    
        
    
def get_guessed_word_hints(letters_guessed, missed_letters) :
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    missedLetters: list (of letters), which have not benn guessed so far
    returns: string, the letter the user entered.
    '''
    global warnings
    correct_input = False
    while True:
        print('Please guess a letter: ')
        guess = input()
        guess.lower()
        if guess == "*":
            correct_input = True
            return guess, correct_input
        else:
            if (guess in letters_guessed) or (guess in missed_letters):
                correct_input = False
                return guess, correct_input

            else:
                if len(guess) == 1:
                    if guess in "abcdefghijklmnopqrstuvwxyz":
                        correct_input = False
                        return guess, correct_input
                else:
                    if guess == "":
                        correct_input = False
                        return guess, correct_input
                    else:
                        correct_input = False
                        return guess, correct_input
        
              
    
def avaliable(missed_letters, letters_guessed):
    missed_letters = set(missed_letters)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    letters = alphabet.difference(missed_letters)
    letters = letters.difference(letters_guessed)

    return letters
    


def get_available_letters(letters_guessed, missed_letters, input_word) :
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    vowel = False
    win = True
    if input_word not in secret_word:
      missed_letters.append(input_word)
      print("\nOops! That letter is not in my word:\n")
      win = False
      if input_word in "aeiou":
          vowel = True
        
    return missed_letters, win, vowel



def get_guessed_letters(letters_guessed, input_word):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    input_word: string, the letter the user entered.
    returns: updated list (of letters), which letters have been guessed so far
    '''
    if input_word in letters_guessed:
      print()
    elif input_word in secret_word:
      letters_guessed.append(input_word)
      print("\nGood guess!\n")
    return letters_guessed


def underscores(secret_word, letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    secret_word: string, the word the user is guessing
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    blankes = []
    for i in range(len(secret_word)):
        blankes.append("_")

    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            blankes[i] = secret_word[i]

    return blankes





def hangman(secret_word) :
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global attempts 
    global missedLetters 
    global letters_guessed
    global warnings

    gameIsDone = is_word_guessed(secret_word, letters_guessed)
     

    if (len(missedLetters) == 0) and (len(letters_guessed) == 0):
        print("\nWelcome to the game Hangman!\nI am thinking of a word that is", len(secret_word), "letters long.\n")
        print("-" * 70)

    if (attempts > 0) and (gameIsDone == True):
        print("\nCongratulations, you won!")

    elif attempts <= 0:
        print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep="")

    elif (attempts > 0) and (gameIsDone == False):

        print("\nYou have", warnings, "warnings left.")
        print("\nYou have", attempts, "guesses left!\n")

        avaliable_letters = avaliable(missedLetters, letters_guessed)
        print('Avaliable letters:')
        for letter in avaliable_letters:
            print(letter, end=' ')
        print()



        guess, correct = get_guessed_word(letters_guessed, missedLetters)

        if correct == False:
            warnings -= 1
            print("\nOops! You've already guessed that letter. You have", warnings, "warnings left.")
        
        if warnings == 0:
            attempts -= 1
            warnings = 3


        letters_guessed = get_guessed_letters(letters_guessed, guess)

        missedLetters, gameround_result, is_vowel = get_available_letters(letters_guessed, missedLetters, guess)

        blanks = underscores(secret_word, letters_guessed)

        print(" ".join(blanks))
        print("\n")
        print("-" * 70)
                
        if gameround_result == False:
            attempts -= 1
        elif is_vowel == True:
            attempts = attempts - 1

        return hangman(secret_word)

        




def match_with_gaps(my_word, other_word) :
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    match = True
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
          if my_word[i] == "_":
            continue
          else:
            if my_word[i] == other_word[i]:
              continue
            else:
              match = False
    else:
      match = False
    
    return match



def show_possible_matches(my_word) :
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    global wordlist

    hint = []
    for word in wordlist:
      matches = match_with_gaps(my_word, word)
      if (matches == True) and (word not in hint):
        hint.append(word)
      else:
        continue

    return hint



def hangman_with_hints(secret_word) :
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    global attempts 
    global missedLetters 
    global letters_guessed
    global warnings
     
    gameIsDone = is_word_guessed(secret_word, letters_guessed)

    if (len(missedLetters) == 0) and (len(letters_guessed) == 0):
        print("\nI am thinking of a word that is", len(secret_word), "letters long.\n")
        print("-" * 70)

    if (attempts > 0) and (gameIsDone == True):
        print("\nCongratulations, you won!")

    elif attempts <= 0:
        print('Sorry, you ran out of guesses. The word was ', secret_word, '.', sep="")

    elif (attempts > 0) and (gameIsDone == False):


        print("\nYou have", warnings, "warnings left.")
        print("\nYou have", attempts, "guesses left!\n")

        avaliable_letters = avaliable(missedLetters, letters_guessed)
        print('Avaliable letters:')
        for letter in avaliable_letters:
            print(letter, end=' ')
        print()




        guess, correct = get_guessed_word_hints(letters_guessed, missedLetters)

        blanks = underscores(secret_word, letters_guessed)

        if guess == "*":
            hints = show_possible_matches(blanks)
            if len(hints) == 0:
                print("Sorry, no similar words were found!")
                hangman_with_hints(secret_word)
            else:
                print("\n\nPossible word matches are: \n")
                for i in range(0, len(hints)):
                    if i % 10 == 9:
                        print(hints[i], end=" \n\n")
                    else:
                        print(hints[i], end="   ")
                print("\n")
                print("-" * 70)
                hangman_with_hints(secret_word)
        

        else:
            if correct == False:
                warnings -= 1
                print("\nOops! You've already guessed that letter. You have", warnings, "warnings left.")
        
            if warnings == 0:
                attempts -= 1
                warnings = 3

            letters_guessed = get_guessed_letters(letters_guessed, guess)

            missedLetters, gameround_result, is_vowel = get_available_letters(letters_guessed, missedLetters, guess)

            blanks = underscores(secret_word, letters_guessed)

            print(" ".join(blanks))

            print("\n")
            print("-" * 70)

            
            if gameround_result == False:
                attempts = attempts - 1
                if is_vowel == True:
                    attempts = attempts - 1
            return hangman_with_hints(secret_word)


        


print('Welcome to the game Hangman!\n')

print("Do you want to be able to see tips during the game? If yes - enter 1, if not - enter 2.\n")
while True:
  gamemode = input("Your choice: ")
  if gamemode == "1":
    hangman_with_hints(secret_word)
    break
  elif gamemode == "2":
    hangman(secret_word)
    break
  elif (gamemode != "1") or (gamemode != "2"):
    print("You have entered an incorrect value. \nTry again:")
  else:
    break



#if __name__ == "__main__" :

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)


