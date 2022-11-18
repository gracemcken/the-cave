import gspread
import time
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


def typePrint(text):
    """
    Alters speed of text to mimic text being typed out.
    """
    text += "\n"
    for char in text:
        time.sleep(0.05)
        print(char, end="", flush=True)


# Game set up functions. Each run at the beginning of the game.


def get_name():
    """
    Gets name of player.
    """
    typePrint("Welcome, wanderer.\n")
    typePrint("What is your name?")
    while True:
        name = input("\nMy name is: ")
        if not name.isalpha():
            typePrint("Please enter letters only.")
            continue
        else:
            typePrint(f"Hello {name}. Welcome to the Cave.")
            break
    return name


def add_name(name):
    """
    Adds player name to character worksheet
    """
    worksheet_to_update = SHEET.worksheet("character")
    worksheet_to_update.update_cell(2, 1, name)


def get_race():
    """
    Player chooses their race, each different option
    add different statistics to the player's core scores
    """

    typePrint("Tell me, what race are you?\n")
    typePrint(
        """
    Human: Adaptable and ambitious, humans are the jack of all trades when it
    comes to races.
    """
    )
    typePrint(
        """
    Elf: Known for their beauty and grace, elves excel at acrobatics and
    swiftness.
    """
    )
    typePrint(
        """
    Dwarf: Solid and stout, dwarves are as stubborn as they are strong.
    """
    )
    while True:
        race = input("My race is: ")
        races = ["human", "dwarf", "elf"]
        if race in races:
            typePrint(f"Nice to meet you, {race}. You are the first {race}")
            typePrint("to be seen here in a long time. Please, give me one")
            typePrint("moment to prepare your tale.")
            break
        else:
            typePrint(
                """
    Please type one of the races listed and ensure to use lowercase.
    """
            )

            continue
    return race


def add_race(race):
    """
    Adds player race to character worksheet
    """
    worksheet_to_update = SHEET.worksheet("character")
    worksheet_to_update.update_cell(2, 2, race)


def get_class():
    """
    Player chooses their class, each different option add
    different statistics to the player's core scores
    """
    typePrint(
        """
    You seem fairly capable of handling yourself. In which area do your
    expertise lie?
    """
    )
    typePrint(
        """
    Warrior: Strong and formidable, well versed in the art of melee combat.
    """
    )
    typePrint(
        """
    Ranger: A hunter, their work depends of their stealth and instincts
    """
    )
    typePrint(
        """
    Mage: Intelligent and shrewd; as long as they have something to channel it,
    they can control magic.
    """
    )

    player_classes = ["warrior", "ranger", "mage"]
    while True:
        player_class = input("My class is: ")
        if player_class in player_classes:
            typePrint(f"Ah, a {player_class}.")
            break
        else:
            typePrint(
                """
                Please type one of the classes listed and ensure to use
                lowercase.
                """
            )
            continue
    return player_class


def add_player_class(player_class):
    """
    Adds player class to character worksheet
    """
    worksheet_to_update = SHEET.worksheet("character")
    worksheet_to_update.update_cell(2, 3, player_class)


def preferred_weapon(player_class):
    """
    Player chooses their preferred weapon, each class has different options.
    """
    typePrint(
        """
    I'm sure you're strong in a fight, but if you had to choose, which weapon
    would be your preference?
    """
    )

    if player_class == "warrior":
        typePrint("Sword")
        typePrint("or")
        typePrint("Axe")
        while True:
            weapon = input("")
            weapons = ["sword", "axe"]
            if weapon in weapons:
                typePrint(f"The mighty {weapon}, of course... of course.")
                break
            else:
                typePrint(
                    """
                    Please type one of the weapons listed and ensure to use
                    lowercase.
                    """
                )
                continue
    elif player_class == "ranger":
        typePrint("Dagger")
        typePrint("or")
        typePrint("Bow")
        while True:
            weapon = input("")
            weapons = ["dagger", "bow"]
            if weapon in weapons:
                typePrint(f"The elegant {weapon}, of course... of course.")
                break
            else:
                typePrint(
                    """
                    Please type one of the weapons listed and ensure to use
                    lowercase.
                    """
                )
                continue
    else:
        typePrint("Staff")
        typePrint("or")
        typePrint("Spell Tome")
        while True:
            weapon = input("")
            weapons = ["staff", "spell tome"]
            if weapon in weapons:
                typePrint(f"The mystical {weapon}, of course... of course.")
                break
            else:
                typePrint(
                    """
                    Please type one of the weapons listed and ensure to use
                    lowercase.
                    """
                )
                continue
    return weapon


def add_preferred_weapon(weapon):
    """
    Adds player weapon to character worksheet
    """
    worksheet_to_update = SHEET.worksheet("character")
    worksheet_to_update.update_cell(2, 4, weapon)


def add_race_modifiers(race):
    """
    Adds onto player's core stats depending on their race.
    Human gets +5 to dexterity and strength.
    Dwarf gets + 10 to strength.
    Elf gets + 10 to dexterity
    """
    if race == "human":
        worksheet_to_update = SHEET.worksheet("character")
        worksheet_to_update.update_cell(2, 7, int(15))
        worksheet_to_update.update_cell(2, 8, int(15))
    elif race == "dwarf":
        worksheet_to_update = SHEET.worksheet("character")
        worksheet_to_update.update_cell(2, 8, int(20))
    else:
        worksheet_to_update = SHEET.worksheet("character")
        worksheet_to_update.update_cell(2, 7, int(20))


def add_class_modifiers(player_class):
    """
    Adds onto player's core stats depending on their class.
    Warrior gets +10 strength.
    Ranger gets + 10 to dexterity.
    Mage gets +10 to luck.
    """
    if player_class == "warrior":
        worksheet_to_update = SHEET.worksheet("character")
        # Call current value of strength and add 10 to it.
        cell_to_update = worksheet_to_update.acell("H2").value
        class_buff = int(cell_to_update) + int(10)
        worksheet_to_update.update_cell(2, 8, int(class_buff))
    elif player_class == "ranger":
        worksheet_to_update = SHEET.worksheet("character")
        # Call current value of dexterity and add 10 to it.
        cell_to_update = worksheet_to_update.acell("G2").value
        class_buff = int(cell_to_update) + int(10)
        worksheet_to_update.update_cell(2, 7, int(class_buff))
    else:
        worksheet_to_update = SHEET.worksheet("character")
        # Call current value of luck and add 10 to it.
        cell_to_update = worksheet_to_update.acell("F2").value
        class_buff = int(cell_to_update) + int(10)
        worksheet_to_update.update_cell(2, 6, int(class_buff))


# End of game start up functions.
