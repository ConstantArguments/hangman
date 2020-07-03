import words
import random

def hangman(word):
    """
    Plays a game of hangman.
    Places each character of word string into list.
    Board shows length of word with placeholders.
    Player guesses letters to complete word before image of hanged body
    and gallows is formed.
    Previously guessed letters are displayed.
    Correct guesses replace all placeholders in board with instance of
    letter.
    :param word: str.
    """
    wrong = 0
    stages = ["            ",
              "____________",
              "|      |    ",
              "|      |    ",
              "|      0    ",
              "|     /|\   ",
              "|      |\   ",
              "|           ",
              "|TXTXTXTXTXT",]
    rletters = list(word)
    guessed = []
    blank = "◊"
    board = [blank] * len(word)
    win = False
    print("Welcome to Hangman!\n")
    print("".join(board))

    while wrong < len(stages) -1:
        print("\n")
        msg = "Guess a Letter: "
        char = input(msg)
        guessed.append(char)
        print(f"You have guessed: {guessed}")
        if char in rletters:
            for i in rletters:
                try:
                    cind = rletters.index(char)
                    board[cind] = char
                    rletters[cind] = "å" # "å" unlikely to be guessed.
                except:
                    continue
        else:
            wrong += 1
        print("".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if blank not in board:
            print("Winner, Winner! Chicken Dinner!\n")
            print("".join(board))
            win = True
            break
    if not win:
        print(f"You lose! It the word was \"{word}\"!")

def get_randword ():
    """
    Returns random word from import words.py.
    """
    randnum = random.randint(0, 999)
    randword = words.wordslist[randnum]
    return randword

hangman(get_randword())
