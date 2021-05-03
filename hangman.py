def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|         |         ",
              "|         |         ",
              "|         o         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to HANGMAN!")


    while wrong < len(stages) -1:
        print("\n")
        msg = "guess a character: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose!! The answer is {}.".format(word))


wordList = [
    "dog",
    "rabbit",
    "cow",
    "horse",
    "wolf",
    "hippopotamus",
    "kangaroo",
    "fox",
    "giraffe",
    "bear",
    "koala",
    "bat",
    "gorilla",
    "rhinoceros",
    "monkey",
    "deer",
    "zebra",
    "jaguar",
    "skunk",
    ]

import random

hangman(wordList[random.randint(0, len(wordList))])
    





    
