import words
import random

def hangman(word):
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

randnum = random.randint(0, 1000)
randword = words.wordslist[randnum]
hangman(randword)
