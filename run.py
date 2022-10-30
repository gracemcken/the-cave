import os
import gspread

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


def default_player_stats():
    """
    Places default player stats into google sheet before any modifications can be made or buffs.
    """
    worksheet_to_update = SHEET.worksheet("character")
    # character's default health points
    worksheet_to_update.update_cell(2, 5, int(100))
    # character's default luck
    worksheet_to_update.update_cell(2, 6, int(10))
    # character's default dexterity
    worksheet_to_update.update_cell(2, 7, int(10))
    # character's default strength
    worksheet_to_update.update_cell(2, 8, int(10))
    # character's default attack
    worksheet_to_update.update_cell(2, 9, int(10))
    # character's default defense
    worksheet_to_update.update_cell(2, 10, int(20))


def get_name():
    """
    Gets name of player.
    """
    print("Welcome, wanderer.\n")
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


def add_name(name):
    """
    Adds player name to character worksheet
    """
    worksheet_to_update = SHEET.worksheet("character")
    worksheet_to_update.update_cell(2, 1, name)


def get_race():
    """
    Player chooses their race, each different option add different statistics to the player's core scores
    """
    print("Tell me, what race are you?\n")
    print(
        "Human: Adaptable and ambitious, humans are the jack of all trades when it comes to races."
    )
    print(
        "Elf: Known for their beauty and grace, elves excel at acrobatics and swiftness."
    )
    print("Dwarf: Solid and stout, dwarves are as stubborn as they are strong.\n")
    while True:
        race = input("My race is: ")
        races = ["Human", "human", "Dwarf", "dwarf", "Elf", "elf"]
        if race in races:
            print(
                f"Nice to meet you, {race}. You are the first {race} to be seen here in a long, long time."
            )
            break
        else:
            print(
                "Please type one of the races listed and ensure there is a capital letter."
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
    Player chooses their class, each different option add different statistics to the player's core scores
    """
    print(
        "You seem fairly capable of handling yourself. In which area do your expertise lie?\n",
        1,
    )
    print("Warrior: Strong and formidable, well versed in the art of melee combat.", 1)
    print("Ranger: A hunter, their work depends of their stealth and instincts", 1)
    print(
        "Mage: Intelligent and shrewd, as long as they have something to channel it, they can control magic.\n"
    )
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
    print(
        "I'm sure you're strong in a fight, but if you had to choose, which weapon would be your preference?\n",
        1,
    )
    if player_class == "warrior" or player_class == "Warrior":
        print("Sword")
        print("or")
        print("Axe")
        while True:
            weapon = input("")
            weapons = ["sword", "Sword", "axe", "Axe"]
            if weapon in weapons:
                print(f"The mighty {weapon}, of course... of course.")
                break
            else:
                print("Please type one of the weapons listed.")
                continue
    elif player_class == "ranger" or player_class == "Ranger":
        print("Dagger")
        print("or")
        print("Bow")
        while True:
            weapon = input("")
            weapons = ["dagger", "Dagger", "bow", "Bow"]
            if weapon in weapons:
                print(f"The elegant {weapon}, of course... of course.")
                break
            else:
                print("Please type one of the weapons listed.")
                continue
    else:
        print("Staff")
        print("or")
        print("Spell Tome")
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
    if race == "Human" or race == "human":
        worksheet_to_update = SHEET.worksheet("character")
        worksheet_to_update.update_cell(2, 7, int(15))
        worksheet_to_update.update_cell(2, 8, int(15))
    elif race == "Dwarf" or race == "dwarf":
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
    if player_class == "warrior" or player_class == "Warrior":
        worksheet_to_update = SHEET.worksheet("character")
        # Call current value of strength and add 10 to it.
        cell_to_update = worksheet_to_update.acell("H2").value
        class_buff = int(cell_to_update) + int(10)
        worksheet_to_update.update_cell(2, 8, int(class_buff))
    elif player_class == "ranger" or player_class == "Ranger":
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


def wake_up():
    """
    Introduction for player, section 1 of the story.
    """
    print("You wake up in a cold, damp cave...\n")
    print("You can't remember the last thing that happened to you but here you are; \n")
    print("Shivering... \n Confused... \n Lost...")
    print("Do you...?")


def start_game():
    """
    Begins game, collecting information such as player name, class, race and preferred weapons.
    """
    default_player_stats()
    name = get_name()
    race = get_race()
    player_class = get_class()
    weapon = preferred_weapon(player_class)
    add_name(name)
    add_race(race)
    add_player_class(player_class)
    add_preferred_weapon(weapon)
    add_race_modifiers(race)
    add_class_modifiers(player_class)
    os.system("clear")
    wake_up()


if __name__ == "__main__":
    start_game()
