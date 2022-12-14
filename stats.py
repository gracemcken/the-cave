import random
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

# Game start up stat functions.


def default_player_stats():
    """
    Places default player stats into google sheet before any modifications can
    be made or buffs.
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


def default_player_inventory():
    """
    Clears worksheet of any previous inventory.
    """
    worksheet_to_update = SHEET.worksheet("inventory")
    worksheet_to_update.clear()


# Game-play stat roll functions.


def roll_dex():
    """
    Gets player's dexterity and rolls extra score.
    """
    worksheet_to_pull = SHEET.worksheet("character")
    dexterity = worksheet_to_pull.acell("G2").value
    dice_roll = random.randint(0, 20)
    final_dex = int(dexterity) + dice_roll
    return final_dex


def roll_luck():
    """
    Gets player's luck and rolls extra score.
    """
    worksheet_to_pull = SHEET.worksheet("character")
    luck = worksheet_to_pull.acell("F2").value
    dice_roll = random.randint(0, 15)
    final_luck = int(luck) + dice_roll
    return final_luck


def roll_strength():
    """
    Gets player's strength and rolls extra score.
    """
    worksheet_to_pull = SHEET.worksheet("character")
    strength = worksheet_to_pull.acell("H2").value
    dice_roll = random.randint(0, 15)
    final_strength = int(strength) + dice_roll
    return final_strength


def roll_attack():
    """
    Gets player's attack and rolls extra score.
    """
    worksheet_to_pull = SHEET.worksheet("character")
    attack = worksheet_to_pull.acell("I2").value
    dice_roll = random.randint(0, 15)
    final_attack = int(attack) + dice_roll
    return final_attack


# Alter player stat functions.


def update_hp(num):
    """
    Updates player's health points.
    """
    worksheet_to_update = SHEET.worksheet("character")
    health = worksheet_to_update.acell("E2").value
    new_health = int(health) - int(num)
    worksheet_to_update.update("E2", int(new_health))
