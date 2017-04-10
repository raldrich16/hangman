# Hangman game


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter in lettersGuessed:
            continue
        else:
            return False
            break
    return True
    




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    mystr = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            mystr += letter
        else:
            mystr += '_ '
    return mystr
    


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avabc = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in avabc:
            avabc.remove(letter)
    return "".join(avabc)

    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    '''
    
    space = '-----------'    
    print('Welcome to the game, Hangman!')
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print(space)    
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessLeft = 8
    guessword = getGuessedWord(secretWord, lettersGuessed)       
    while guessLeft>0:
        print("You have " + str(guessLeft) + " guesses left.")
        print("Available letters: " + str(availableLetters))
        guess = input("Please guess a letter: ").lower()
        if guess in availableLetters:        
            lettersGuessed.append(guess)
            availableLetters = getAvailableLetters(lettersGuessed)            
            guessword = getGuessedWord(secretWord, lettersGuessed)
            if guess in secretWord:
                print('Good guess: ' + guessword)
                print(space)                
                if '_' not in guessword:
                    print('Congratulations, you won!')
                    break
            else:
                print('Oops! that letter is not in my word:' + guessword )
                print(space)                
                guessLeft -= 1
                if guessLeft == 0:
                    print("Sorry, you ran out of guesses. The word was " + secretWord + '.')
        elif guess not in availableLetters:
            print("Oops!  You've already guessed that letter: " + guessword)
            print(space)
        






secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
