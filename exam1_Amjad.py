import random
import sys
menu = """
Please,
 enter "r/R" for Rock
 enter "p/P" for Paper
 enter "s/S" for Scissors
"""
menu_again = """
DO you want to play again?
Please,
1)Enter "Yes" to play again
2)Press any key to exit the game
"""


def get_name():
    user_name0 = input("Hello, Please enter your name: ")
    print(f"You entered {user_name0} as your name")
    menu_name = f"""
    PLEASE, Enter:
    'yes' to play as {user_name0} .
    'C' to change the name. 
    """
    while True:
        n = input(f"{menu_name}")
        if n in ["yes", "YES", "Yes"]:
            return user_name0
        elif n in ["c", "C"]:
            user_name0 = input("Hello, Please re-enter your name:  ")
            return user_name0
        else:
            print("INVALID CHOICE")


def get_rps():
    while True:
        user_choice = input(menu)
        if user_choice in ["r", "R", "p", "P", "s", "S"]:
            if user_choice in ["r", "R"]:
                print("you played ROCK!")
                return "r"
            elif user_choice in ["p", "P"]:
                print("you played PAPER!")
                return "p"
            else:
                print("you played SCISSOR!")
                return "s"
        else:
            print(f"Please, make sure to choose from the menu --> {menu}")


def get_ai():
    list1 = ["r", "R", "p", "P", "s", "S"]
    AI_choice = random.choice(list1)
    if AI_choice in ["r", "R"]:
        print("AI played ROCK!")
        return "r"
    elif AI_choice in ["p", "P"]:
        print("AI played PAPER!")
        return "p"
    else:
        print("AI played SCISSOR!")
        return "s"


def get_winner(c1, c2):          # Adding some comments ONLY when the user wins
    if c1 == "r" and c2 == "s":
        print("ROCK BREAKS SCISSOR")
        return 1
    elif c1 == "s" and c2 == "p":
        print("SCISSOR CUTS PAPER")
        return 1
    elif c1 == "p" and c2 == "r":
        print("PAPER WRAPS ROCK")
        return 1
    elif (c2 == "r" and c1 == "s") or (c2 == "s" and c1 == "p") or (c2 == "p" and c1 == "r"):
        return 2
    else:
        return None


print("***Welcome to this simple version of Rock, Paper, and Scissors***")
user_name = get_name()
player_count = 0
playerAI_count = 0
while True:
    player = get_rps()
    player_AI = get_ai()
    x = get_winner(player, player_AI)
    if x == 1:                    # you may use function here
        print(f"{user_name} YOU WON !")
        player_count = player_count + 1
        print(f"{user_name} won {player_count} times VS AI won {playerAI_count} times")
    elif x == 2:
        print(f"{user_name} YOU LOST!")
        playerAI_count = playerAI_count + 1
        print(f"{user_name} won {player_count} times VS AI won {playerAI_count} times")
    else:
        print("It's a tie")
        print(f"{user_name} won {player_count} times VS AI won {playerAI_count} times")
    again = input(menu_again)
    if again in ["yes", "Yes"]:
        continue
    else:
        print(f"FINAL RESULT: {user_name} won {player_count} times VS AI won {playerAI_count} times")
        print("SEE YOU SOON, GOODBYE!")
        sys.exit()     # instead of break
