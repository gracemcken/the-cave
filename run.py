import os
import gspread
from google.oauth2.service_account import Credentials
import character
import stats as stat
import events as event
import variables


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("the_cave")


def intro():
    """
    Shows artwork and introduces the game.
    """
    print(
        r"""
_________          _______    _______  _______           _______
\__   __/|\     /|(  ____ \  (  ____ \(  ___  )|\     /|(  ____ \
   ) (   | )   ( || (    \/  | (    \/| (   ) || )   ( || (    \/
   | |   | (___) || (__      | |      | (___) || |   | || (__
   | |   |  ___  ||  __)     | |      |  ___  |( (   ) )|  __)
   | |   | (   ) || (        | |      | (   ) | \ \_/ / | (
   | |   | )   ( || (____/\  | (____/\| )   ( |  \   /  | (____/\
   )_(   |/     \|(_______/  (_______/|/     \|   \_/   (_______/
"""
    )
    print(
        """
        Welcome to The Cave, a text based adventure game where your choices at
        the beginning of the game impact the outcome of the end. Along with
        your stats that are generated based on your choices, there is also
        a random dice roll added, just like in Dungeons and Dragons!
        Please press enter to begin!
        """
    )
    while True:
        input1 = input("Press ENTER: ")
        if input1 == "":
            print("The game will now begin!")
            start_game()
        else:
            print(f"You typed '{input1}'. The game will not start yet.")
            continue


# Beginning of game-play below.


def start_game():
    """
    Begins game, collecting information such as player name, class, race and
    preferred weapons.
    """
    stat.default_player_stats()
    stat.default_player_inventory()
    os.system("clear")
    variables.initialize_variables()
    character.add_name(variables.name)
    character.add_race(variables.race)
    character.add_player_class(variables.player_class)
    character.add_preferred_weapon(variables.weapon)
    character.add_race_modifiers(variables.race)
    character.add_class_modifiers(variables.player_class)
    os.system("clear")
    answer1 = event.wake_up()
    os.system("clear")
    event.decision_one(answer1)


if __name__ == "__main__":
    intro()
