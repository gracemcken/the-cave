import os

import gspread
from google.oauth2.service_account import Credentials
import stats as stat
from run import start_game


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
            print("Thankfully by carefully walking slowly,")
            print("you manage to make your way towards the light")
            print("without incident. You can now see your")
            print("surroundings a little better.")
            stage_2()
        else:
            fail_one()
    elif answer1 == "2":
        luck = stat.roll_luck()
        if luck >= 15:
            find_item_one()
        else:
            fail_two()
    else:
        print("You close your eyes and fall asleep.\n")
        print("The game is over. You will never know what could have been.")
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
    should the player fail the first option
    in the first choice.
    """
    stat.update_hp(5)
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


def fail_two():
    """
    Function that decides what happens
    should the player fail the second option
    of the first choice.
    """
    stat.update_hp(5)
    print("As you feel around, your hands meet the rough")
    print("edge of the stone wall. 'Success!' you think.")
    print("Surely you can use this as a way to safely navigate")
    print("to the exit. Instead, you cut open your hand")
    print("on a sharp bit of rock jutting out from the wall.\n")
    print("You lose 5 health points.\n")
    print("Do you...?\n")
    print("1. Stand up and continue towards the light.\n")
    print("2. Continue feeling around the area.\n ")
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
    Scene 2 of the story and next decision.
    """
    print("The source of the light is a iron lantern fixed to the wall.")
    print("The cave seems to be starting to form into a carved out hallway,")
    print("with more lanterns lining the pathway down.")
    worksheet_to_pull = SHEET.worksheet("inventory")
    inventory = worksheet_to_pull.col_values(1)
    if "torch" in inventory:
        print("You already have a light source thankfully, but the")
        print("lanterns provide an extra bit of light for you. You")
        print("continue down the corridor, following the more")
        print("structured pathway.")
        stage_3()
    else:
        print("While the lanterns seem to continue down the hallway,")
        print("you have no idea whether further along the path is lit.\n")
        print("Do you...?\n")
        print("1. Attempt to hoist one of the lanterns from the wall.\n")
        print("2. Ignore them and continue on down the hall.")
        print("3. Close your eyes again and wish for this game to end.\n")
        print("Please choose a option number\n")
        while True:
            answer2 = input("")
            answers = ["1", "2", "3"]
            if answer2 in answers:
                print(
                    f"You have chosen option {answer2}."
                    " Let us see if the odds are in your favour..."
                )
            else:
                print("Please type either '1', '2', or '3'.")
                continue
            return answer2


def find_item_one():
    """
    Text that runs if the player successfully passes the luck check. Results in
    torch and rusted key being added to inventory.
    """
    print("Success! You're not sure if it's just luck or someone")
    print("is looking out for you, but as your hands feel around")
    print("the floor in front of you, you come into contact with")
    print("what feels like a satchel. Inside you find what you can assume")
    print("is a torch and some flint, along with what seems to be a rusted key.\n")
    print("You pocket the key for now and light your new torch, illuminating the")
    print("cave around you. The area is littered with sharp rocks and little")
    print("else. You are lucky to now be able to see where you go.\n")
    print(
        "With your new items in your inventory, you set off safely towards the light."
    )
    worksheet_to_update = SHEET.worksheet("inventory")
    worksheet_to_update.update_cell(1, 1, "torch")
    worksheet_to_update.update_cell(2, 1, "rusted key")

    stage_2()


def stage_3():
    """
    Scene 3 of the story and next decision.
    """
    print("Scene 3")


def stage_4():
    """
    Scene 4 of the story and next decision.
    """
    print("Scene 4")


def stage_5():
    """
    Scene 5 of the story and next decision.
    """
    print("Scene 5")
