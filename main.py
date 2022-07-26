# pip install random-words
import os
from random_word import RandomWords
from utilities.hangman import hangman
random = RandomWords().get_random_word(maxLength=10)
preGuessed = []
wrongEntries = 0

clear = lambda: os.system('clear')


def displayGuessedWord():
    display = []
    for i in range(len(random)):
        if random[i] in preGuessed:
            display.append(random[i])
        else:
            display.append('_')
    print(display)
    


def displayHangman():
    print(hangman[wrongEntries])


while wrongEntries < 7:
    displayHangman()
    displayGuessedWord()
    guessedLetter = input("\n\nEnter the guess letter: ")
    clear()
    if guessedLetter in random:
        if guessedLetter not in preGuessed:
            preGuessed.append(guessedLetter)
            print(f"\nCorrect Guess !!\nGuesses Remaining: {7 - wrongEntries}")
        else:
            wrongEntries += 1
    else:
        wrongEntries += 1
        print("Wrong guess")
        print(f"You have {7 - wrongEntries} guesses left")
    if len(preGuessed) == len(random):
        print("You won!!")
        break

print(f"Game Over. The word was {random}")


