#HangMan 1/8/2024


import random
HANGMAN_PICS = [
    
    '''
    +---+
        |
        |
        |
       === ''','''
    +---+
    0   |
        |
        |
       === ''', '''
    +---+
    0   |
    |   |
        |
       === ''','''
    +---+
    0   |
   /|   |
        |
       === ''','''
    +---+
    0   |
   /|\  |
        |
       === ''', '''
    +---+
    0   |
   /|\  |
   /    |
       === ''', '''
    +---+
    0    |
   /|\   |
   / \  |
       === ''']

words = 'ant babboon badger bat beaver bear camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret for frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spide stork swan tiger toad trout turcky turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(alist):
    wordIndex = random.randint(0, len(alist) -1)
    return alist[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end ='')
    for letter in missedLetters:
        print(letter, end ='')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end ='')
    print()
    
def getGuess(alreadyGuessed):
    while True:
        print("Guess a Letter")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please Enter A Single Letter")
        elif guess in alreadyGuessed:
            print("You Have Already Guessed That Letter Guess Again ")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please Enter A Letter")
        else:
            return guess
        
def playAgain():
    print("Do You Wish To Play Again? (Yes or No)")
    return input().lower().startswith('y')

print("H A N G M A N")
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False


while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print(f"Yes! You have guessed all the letter in the word {secretWord} Great job you win!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(f"You ran out of guesses. The answer was {secretWord} better luck next time!")
            gameIsDone = True

        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break




