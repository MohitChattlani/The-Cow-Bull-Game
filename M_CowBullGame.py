import random

def set_word():
    a = open("Wordlist.txt", "r")
    b = random.randrange(92)
    s=""
    for i in range(b):
        s = a.readline()
    a.close()
    return(s[0:4])

def input_word(c):
    print("\nEnter your guess no. " + str(c+1))
    guess = input().upper()
    if len(guess)<4:
        print("Wrong Input: Length of word is too short.")
        return("XXXX")
    else:
        for i in range(3):
            if guess[i] in guess[i+1:4]:
                print("Wrong Input: One or more letters are being repeated in the first 4 letters of your input")
                return("XXXX")
        return(guess[0:4])

def print_result(b, c):
    print("Bulls = " + str(b))
    print("Cows = " + str(c))

def again(turns, total_score, n):
    print("\nDo you want to play again? Enter 'YES' to play again or anything else to terminate the program: ")
    play_again = input().upper()
    if play_again == 'YES':
        start_game(turns, total_score, n)
    else:
        print("Game terminated")

def print_rules():
    print("\nRULES AND INFO:\n")
    print("A word has been chosen by this program. It is a 4-letter meaningful word.\nIt is neither a proper noun nor an abbreviation. You have 10 chances to guess that word.")
    print("All of your guess must be 4-letter words with no letter repeated in a single word.")
    print("If you enter more than 4 letters, only first four would be considered")
    print("No. of Bulls obtained after each guess denotes the no. of letters that exist in both your guess and the word to be guessed with identical position of occurrence.")
    print("No. of Cows obtained after each guess denotes the no. of letters that exist in both your guess and the word to be guessed but with dissimilar positions.\n")

def set_difficulty():
    print("\nSelect your Difficulty Level:\n\nEnter 'E' for Easy\n (12 chances for every word but less points there to earn)\n\nEnter 'M' for Medium\n (10 chances for every word but moderate points there to earn)\n\nEnter 'H' for Hard\n (8 chances for every word but more points there to earn)\n")
    while 1:
        n = input().upper()
        if n=='E':
            print("\nDifficulty set: EASY")
            return(12)
        elif n=='M':
            print("\nDifficulty set: MEDIUM")
            return(10)
        elif n=='H':
            print("\nDifficulty set: HARD")
            return(8)
        else:
            print("\nInvalid Input.")

def start_game(turns, total_score, n):
    word=set_word()
    while len(word)!=4:
        word=set_word()
    turns = turns + 1
    user_input = ""
    mult = 1
    if n==8:
        mult = 2
    elif n==10:
        mult = 1.5
    elif n==12:
        mult = 1
    for count in range(n):
        B = 0
        C = 0
        user_input = input_word(count)
        if user_input == "XXXX":
            continue
        for i in range(4):
            if user_input[i] in word:
                if word.index(user_input[i])==i:
                    B = B + 1
                else:
                    C = C + 1
        print_result(B, C)
        if B == 4:
            print("Hooray!! Game won in " + str((count + 1)) + " guesses.")
            print("Your score in this round is " + str((n - count)*mult) + ".")
            total_score = total_score + (n - count)*mult
            print("Your average score is: " + str(total_score/turns) + " in " + str(turns) + " rounds.")
            break
    if count == n-1 and B!=4:
        print("Oops..! You failed to guess the word in " + str(n) +" chances.\nThe correct answer is " + word + ".\n")
        print("Your average score is: " + str(total_score/turns) + " in " + str(turns) + " rounds.")
    again(turns, total_score, n)
    
print("Welcome to the COW BULL Game!")
print("\nEnter 'START' to initiate the game or anything else to terminate the program: ")
start = input().upper()
if start[0:5] == 'START':
    n = set_difficulty()
    if n==8 or n==10 or n==12:
        print_rules()
        start_game(0, 0, n)
    else:
        print("Game failed to initialise.")
else:
    print("Game failed to initialise.")
