import gspread
import time
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("the_cave")


def fprint(str, delay=0):
    """
    Alters speed of text. Source: Elijah Henderson
    """
    print("\n" + str)
    time.sleep(delay)

def get_name():
    fprint("Welcome, wanderer.\n",1)
    print("What is your name?")
    while True:
        name = input("\n> ")
        if not name.isalpha():
            print("Please enter letters only.")
            continue
        else:
            print(f"Hello {name}. Welcome to the Cave.")
            break
    return name

def add_name():
    """
    Adds player name to character worksheet
    """
    worksheet_to_update = SHEET.worksheet('character')
    worksheet_to_update.update_cell(2,1, name)
    

def get_race():
    """
    Player chooses their race, each different option add different statistics to the player's core scores
    """
    fprint("Tell me, what race are you?\n", 1)
    fprint("Human: Adaptable and ambitious, humans are the jack of all trades when it comes to races.", 1)
    fprint("Elf: Known for their beauty and grace, elves excel at acrobatics and swiftness.", 1)
    fprint("Dwarf: Solid and stout, dwarves are as stubborn as they are strong.\n", 1)
    while True:
        race = input("My race is: ")
        races = ["Human", "Dwarf", "Elf"]
        if race in races:
            print(f"Nice to meet you, {race}. You are the first {race} seen here in a long time.")
            break
        else:
            print("Please type one of the races listed and ensure there is a capital letter.")
            continue
    return race

def add_race():
    """
    Adds player race to character worksheet
    """
    worksheet_to_update = SHEET.worksheet('character')
    worksheet_to_update.update_cell(2,2, race)
    





name = get_name()
race = get_race()
add_name()
add_race()



