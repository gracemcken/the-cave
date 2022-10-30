import os
import gspread
import stats as stat
from run import start_game


from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("the_cave")


def wake_up():
    """
    Introduction for player, section 1 of the story.
    """
    print("You wake up in a cold, damp cave...\n")
    print("You can't remember the last thing that happened to you but here you are; \n")
    print("Shivering... \n Confused... \n Lost...\n")
    print(
        "In the distance you can see a faint glow of light several metres ahead of you."
    )
    print("Do you...?")
    print(
        "1. Stand up and head directly towards the light,\n"
        "despite being unable to see your surroundings.\n"
    )
    print("2. Feel around the area for any item that could be of use to you.\n")
    print("3. Close your eyes again and wish for this game to end.\n")
    print("Please choose a option number\n")
    while True:
        answer1 = input("")
        answers = ["1", "2", "3"]
        if answer1 in answers:
            print(
                f"You have chosen option {answer1}."
                " Let us see if the odds are in your favour..."
            )
        else:
            print("Please type either '1', '2', or '3'.")
            continue
        return answer1


def decision_one(answer1):
    """
    Generates outcome of first decision in game
    """
    if answer1 == "1":
        dex = stat.roll_dex()
        if dex >= 25:
            stage_2()
        else:
            fail_one()
    elif answer1 == "2":
        luck = stat.roll_luck()
        if luck >= 15:
            stage_2()
        else:
            fail_two()
    else:
        print("You close your eyes and fall asleep.\n")
        print("The game is over. You will never know what could have been.")
        os.system("clear")
        print("Want to start again? Please type yes or no")
        user_ans = input("")
        if user_ans == "Yes" or user_ans == "yes":
            start_game()
        elif user_ans == "No" or user_ans == "no":
            print("GAME OVER. THANK YOU FOR PLAYING.")
        else:
            print("Please type either yes/Yes or no/No")


def fail_one():
    """
    Function that decides what happens
    should the player fail the first choice.
    """
    print("Bang! You trip over something and land on your hands")
    print("and knees. It's painful and although you can't see it,")
    print("you can feel blood trickle down the palms of your hands.\n")
    print("You lose 5 health points.\n")
    print("Do you...?")
    print("1. Stand up and continue towards the light.\n")
    print("2. Feel around the area for any item that could be of use to you.\n ")
    print("3. Close your eyes again and wish for this game to end.\n")
    while True:
        answer1 = input("")
        answers = ["1", "2", "3"]
        if answer1 in answers:
            print(
                f"You have chosen option {answer1}."
                " Let us see how you fare this time..."
            )
            decision_one(answer1)
        else:
            print("Please type either '1', '2', or '3'.")
            continue
        return answer1


def stage_2():
    """
    Next stage of the story.
    """
    print("The source of the light is a iron lantern fixed to the wall.")
    print("The cave seems to be starting to form into a carved out hallway,")
    print("with more lanterns lining the pathway down.")
