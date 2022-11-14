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


# Beginning of game-play below.


def start_game():
    """
    Begins game, collecting information such as player name, class, race and
    preferred weapons.
    """
    stat.default_player_stats()
    stat.default_player_inventory()
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
    start_game()
