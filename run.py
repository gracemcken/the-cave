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
    


name = get_name()
add_name()


