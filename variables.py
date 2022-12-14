import gspread
from google.oauth2.service_account import Credentials
import character as char_setup

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("the_cave")

# Makes these vars global throughout application

name = ""
player_class = ""
weapon = ""
race = ""


def initialize_variables():
    global name
    name = char_setup.get_name()
    global player_class
    player_class = char_setup.get_class()
    global weapon
    weapon = char_setup.preferred_weapon(player_class)
    global race
    race = char_setup.get_race()
