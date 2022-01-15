import random
import string

words = ['python', 'java', 'kotlin', 'javascript']
puzzle = random.choice(words)
puzzle_duplicate = []
tries = []
mistaken_tries = []

print("H A N G M A N")


def game():
    global puzzle
    global puzzle_duplicate
    global tries
    global mistaken_tries
    attempts = 8
    while attempts >= 0:
        if attempts > 0:
            for char in puzzle:
                if char in tries:
                    puzzle_duplicate.append(char)
                else:
                    puzzle_duplicate.append("-")
            print()
            print("".join(puzzle_duplicate))
        if attempts == 0 and "".join(puzzle_duplicate) != puzzle:
            print("You lost!")
            print()
            words.remove(puzzle)
            break
        elif attempts >= 0 and "".join(puzzle_duplicate) == puzzle:
            print("You guessed the word!")
            print("You survived!")
            print()
            words.remove(puzzle)
            break
        letter = input("Input a letter: ")
        if len(letter) == 1 and letter in string.ascii_lowercase:
            if letter in puzzle and letter not in tries:
                tries.append(letter)
            elif letter not in puzzle and letter not in mistaken_tries:
                print("That letter doesn't appear in the word")
                attempts -= 1
                mistaken_tries.append(letter)
            elif letter in mistaken_tries or letter in tries:
                print("You've already guessed this letter")
        elif len(letter) != 1:
            print("You should input a single letter")
        elif letter not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        puzzle_duplicate = []

while True:
    question = input('Type "play" to play the game, "exit" to quit: ')
    if question == "play":
        puzzle = random.choice(words)
        puzzle_duplicate = []
        tries = []
        mistaken_tries = []
        game()
    else:
        break
