# Hangman game
import random

WORDLIST_FILENAME = "words.txt"



def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    inFile.close()
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    c=0
    for i in secretWord:
        if i in lettersGuessed:
            c+=1
    if c==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s=[]
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans=''
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    ans=list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)


def pointGain(points):
    points += 5
    return points

def pointLoss(points):
    points -= 2
    return points


def hangman(secretWord, winCount):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    winCount = 0
    points = 0
    
    global lettersGuessed
    mistakeMade=0
    lettersGuessed=[]
    
    while 8 - mistakeMade > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            anotherGame=input("Do you want to play another game? Press Y for yes and N for No: ")

            if(anotherGame=="Y" or anotherGame=="y"):
                winCount=winCount+1
                secretWord = chooseWord(wordlist).lower()
                hangman(secretWord,winCount)
            else:
                break


            
        else:
            print("-------------")
            print(secretWord)
            print(str(lettersGuessed))
            print("Win Count: "+ str(winCount))
            print("Points: "+ str(points))
            print("You have",8-mistakeMade,"guesses left.")
            print("Available letters:",getAvailableLetters(lettersGuessed))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
                
            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
                a = pointGain(points)
                points = a
                print(points)
                
            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed))
                if points >= 2:
                    a = pointLoss(points)
                    points = a
                    print(points)
                
        if 8 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",secretWord)
            anotherGame = input("Do you want to play another game? Press Y for yes and N for No: ")

            if (anotherGame == "Y" or anotherGame=="y"):
                winCount = 0
                secretWord = chooseWord(wordlist).lower()
                hangman(secretWord, str(winCount))
            else:
                break
        
        else:
            continue



secretWord = chooseWord(wordlist).lower()
hangman(secretWord,0)

