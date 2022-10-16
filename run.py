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

def default_player_stats():
    """
    Places default player stats into google sheet before any modifications can be made or buffs.
    """
    worksheet_to_update = SHEET.worksheet('character')
    # character's default health points
    worksheet_to_update.update_cell(2,5, int(100)) 
    # character's default luck
    worksheet_to_update.update_cell(2,6, int(10))
    # character's default dexterity
    worksheet_to_update.update_cell(2,7, int(10))
    # character's default strength
    worksheet_to_update.update_cell(2,8, int(10))
    # character's default attack
    worksheet_to_update.update_cell(2,9, int(10))
    # character's default defense
    worksheet_to_update.update_cell(2,10, int(20))


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
        races = ["Human", "human", "Dwarf", "dwarf", "Elf", "elf"]
        if race in races:
            print(f"Nice to meet you, {race}. You are the first {race} to be seen here in a long, long time.")
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
    

def get_class():
    """
    Player chooses their class, each different option add different statistics to the player's core scores
    """
    fprint("You seem fairly capable of handling yourself. In which area do your expertise lie?\n", 1)
    fprint("Warrior: Strong and formidable, well versed in the art of melee combat.", 1)
    fprint("Ranger: A hunter, their work depends of their stealth and instincts", 1)
    fprint("Mage: Intelligent and shrewd, as long as they have something to channel it, they can control magic.\n", 1)
    while True:
        player_class = input("My class is: ")
        player_classes = ["warrior", "ranger", "mage", "Warrior", "Ranger", "Mage"]
        if player_class in player_classes:
            print(f"Ah, a {player_class}.")
            break
        else:
            print("Please type one of the classes listed.")
            continue
    return player_class

def add_player_class():
    """
    Adds player class to character worksheet
    """
    worksheet_to_update = SHEET.worksheet('character')
    worksheet_to_update.update_cell(2,3, player_class)


def preferred_weapon(player_class):
    """
    Player chooses their preferred weapon, each class has different options.
    """
    fprint("I'm sure you're strong in a fight, but if you had to choose, which weapon would be your preference?\n", 1)
    if player_class == "warrior" or player_class == "Warrior":
        fprint("Sword")
        fprint("or")
        fprint("Axe")
        while True:
            weapon = input(" ")
            weapons = ["sword", "Sword", "axe", "Axe"]
            if weapon in weapons:
                print(f"The mighty {weapon}, of course... of course.")
                break
            else:
                print("Please type one of the weapons listed.")
                continue
    elif player_class == "ranger" or player_class =="Ranger":
        fprint("Dagger")
        fprint("or")
        fprint("Bow")
        while True:
            weapon = input(" ")
            weapons = ["dagger", "Dagger", "bow", "Bow"]
            if weapon in weapons:
                print(f"The elegant {weapon}, of course... of course.")
                break
            else:
                print("Please type one of the weapons listed.")
                continue
    else:
        fprint("Staff")
        fprint("or")
        fprint("Spell Tome")
        while True:
            weapon = input("")
            weapons = ["staff", "Staff", "spell tome", "Spell Tome"]
            if weapon in weapons:
                print(f"The mystical {weapon}, of course... of course.")
                break
            else:
                print("Please type one of the weapons listed.")
                continue
    return weapon


def add_preferred_weapon():
    """
    Adds player weapon to character worksheet
    """
    worksheet_to_update = SHEET.worksheet('character')
    worksheet_to_update.update_cell(2,4, weapon)





default_player_stats()
name = get_name()
race = get_race()
player_class = get_class()
weapon = preferred_weapon(player_class)
add_name()
add_race()
add_player_class()
add_preferred_weapon()



