import random

import gspread
from google.oauth2.service_account import Credentials

import stats as stat
import variables
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

# SCENE 1 POTENTIAL EVENTS


def wake_up():
    """
    Introduction for player, section 1 of the story.
    """
    print(
        """
    You wake up in a cold, damp cave...
    You can't remember the last thing that happened to you, but here you are;
    Shivering...
    Confused...
    Lost...
    In the distance you can see a faint glow of light ahead of you.
    """
    )
    print(
        """
    Do you...?
    1. Stand up and head directly towards the light despite being unable to
    see your surroundings?
    2. Feel around the area for any item that could be of use to you?
    3. Close your eyes again and wish for this game to end.
    """
    )

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


def exit_game():
    exit = """
    You close your eyes and fall asleep.
    The game is over. You will never know what could have been.
    Want to start again? Please type yes or no.
    """
    print(exit)
    user_ans = input("")
    if user_ans == "Yes" or user_ans == "yes":
        start_game()
    elif user_ans == "No" or user_ans == "no":
        print("GAME OVER. THANK YOU FOR PLAYING.")
    else:
        print("Please type either yes/Yes or no/No")


def decision_one(answer1):
    """
    Generates outcome of first decision in game
    """
    if answer1 == "1":
        dex = stat.roll_dex()
        if dex >= 25:
            print(
                """
            Thankfully by carefully walking slowly, you manage to make your way
            towards the light without incident. You can now see your
            surroundings a little better.
            """
            )
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
        exit_game()


# Stat roll failure events below:


def fail_one():
    """
    Function that decides what happens
    should the player fail the first option
    in the first choice.
    """
    stat.update_hp(5)
    print(
        """
    Bang! You trip over something and land on your hands and knees. It's
    painful and although you can't see it, you can feel blood trickle down the
    palms of your hands.
    You lose 5 health points.
    """
    )
    print(
        """
    Do you...?
    1. Stand up and continue towards the light.
    2. Feel around the area for any item that could be of use to you.
    3. Close your eyes again and wish for this game to end.
    """
    )

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
    print(
        """
    As you feel around, your hands meet the rough edge of the stone wall.
    'Success!' you think. Surely you can use this as a way to safely navigate
    to the exit. Instead, you cut open your hand on a sharp bit of rock jutting
    out from the wall.
    You lose 5 health points.
    """
    )
    print(
        """
    Do you...?
    1. Stand up and continue towards the light.
    2. Continue feeling around the area.
    3. Close your eyes again and wish for this game to end.
    """
    )

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


# Potential item pick up scene event, only
# triggers if player passes stat roll after
# choosing option 2 in scene 1.


def find_item_one():
    """
    Text that runs if the player successfully passes the luck check. Results in
    torch and rusted key being added to inventory.
    """
    print(
        """
    Success! You're not sure if it's just luck or someone is looking out for
    you, but as your hands feel around the floor in front of you, you come into
    contact with what feels like a satchel. Inside you find what you can assume
    is a torch and some flint, along with what seems to be a rusted key.
    You pocket the key for now and light your new torch, illuminating the cave
    around you. The area is littered with sharp rocks and little else.
    You are lucky to now be able to see where you go.
    With your new items in your inventory, you set off safely towards the
    light.
    """
    )

    worksheet_to_update = SHEET.worksheet("inventory")
    worksheet_to_update.update_cell(1, 1, "torch")
    worksheet_to_update.update_cell(2, 1, "rusted key")

    stage_2()


# END OF SCENE 1 EVENTS

# SCENE 2 POTENTIAL EVENTS


def stage_2():
    """
    Scene 2 of the story and next decision.
    """
    print(
        """
    The source of the light is a iron lantern fixed to the wall.
    The cave seems to be starting to form into a carved out hallway with more
    lanterns lining the pathway down.
    """
    )

    worksheet_to_pull = SHEET.worksheet("inventory")
    inventory = worksheet_to_pull.col_values(1)
    if "torch" in inventory:
        print(
            """
        You already have a light source thankfully, but the lanterns provide an
        extra bit of light for you. You continue down the corridor, following
        the more structured pathway.
        """
        )

        stage_3()
    else:
        print(
            """
        While the lanterns seem to continue down the hallway, you have no idea
        whether further along the path is lit.
        Do you...?
        1. Attempt to hoist one of the lanterns from the wall.
        2. Ignore them and continue on down the hall.
        3. Close your eyes again and wish for this game to end.
        Please choose a option number
        """
        )

        while True:
            answer2 = input("")
            answers = ["1", "2", "3"]
            if answer2 in answers:
                print(
                    f"You have chosen option {answer2}."
                    " Let us see if the odds are in your favour..."
                )
                decision_two(answer2)
            else:
                print("Please type either '1', '2', or '3'.")
                continue
            return answer2


def decision_two(answer2):
    """
    Generates outcome of second decision in game
    """
    if answer2 == "1":
        strength = stat.roll_strength()
        if strength >= 25:
            print(
                """
            With all of your strength, you attempt to pull the lantern from
            the wall without smashing the glass and burning your hand.
            You hear a clunk as the metal detaches from its place in the wall
            and the lantern comes off in your hand intact and still lit.
            Congratulations! You now have a portable light source! This will
            surely be useful!
            With your new light in hand, you continue down the hall.
            """
            )

            worksheet_to_update = SHEET.worksheet("inventory")
            worksheet_to_update.update_cell(3, 1, "lantern")
            stage_3()
        else:
            fail_three()
    elif answer2 == "2":
        print(
            """
        Hopefully the lanterns continue lighting your way. You're taking a risk
        but also avoiding potential injury. With that decided, you continue
        down the hall.
        """
        )

        stage_3()
    else:
        exit_game()


# Stat roll failure event for scene 2.


def fail_three():
    """
    Function that decides what happens
    should the player fail the only option
    in scene 2.
    """
    stat.update_hp(10)
    print(
        """
    The lantern is wedged into the wall much deeper than you expected. You put
    all your strength into it and pull but unfortunately one of your hands
    slips and crushes the glass inside the lantern. Shards of glass and hot
    candle wax cover your hand, burning and cutting it.
    You lose 10 health points.
    """
    )
    print(
        """
    Do you...?
    1. Admit defeat due to your injured hand and continue down the hall,
    relying on the wall light sources?
    2. Close your eyes again and wish for this game to end.
    """
    )

    while True:
        answer2 = input("")
        answers = ["1", "2"]
        if answer2 in answers:
            print(f"You have chosen option {answer2}.")
            if answer2 == "1":
                stage_3()
            else:
                exit_game()
        else:
            print("Please type either '1' or '2'")
            continue
        return answer2


# END OF SCENE 2 EVENTS

# SCENE 3 POTENTIAL EVENTS

# Main event


def stage_3():
    """
    Scene 3 of the story and next decision.
    """
    print(
        """
    As you reach the end of the hallway, you come across a skeleton propped up
    against the wall. Cobwebs cover his eye sockets, so who knows how long he
    has been there. He seems to be dressed in pieces of iron armour over his
    tattered cloth clothes. The pieces of armour seem to be simply secured by
    straps, so it would be possible for you to remove them and place them on
    yourself for protection. While slightly rusty, they would still stop an
    arrow. It's possible that he may also have a weapon on him judging by his
    state of dress, but you would have to move him to search better.
    """
    )
    print(
        """
    Do you...?
    1. Search him for a weapon.
    2. Remove his armour and strap it to yourself for protection.
    3. Close your eyes again and wish for this game to end.
    Please choose a option number.
    """
    )

    while True:
        answer3 = input("")
        answers = ["1", "2", "3"]
        if answer3 in answers:
            print(f"You have chosen option {answer3}.")
        else:
            print("Please type either '1', '2', or '3'.")
            continue
        if answer3 == "1":
            decision_3_a(variables.player_class)
        elif answer3 == "2":
            decision_3_b()
        else:
            exit_game()


# Decision events


def decision_3_a(player_class):
    """
    What happens should the player choose to select the weapon.
    """
    print(
        """
    You shove the skeleton over to check underneath him for a weapon.
    Unfortunately the he is heavier than he looks and the weight of his armour
    and bones causes the straps of his armour to snap. While that now may be
    unusable, you've thankfully found a weapon.
    """
    )
    if player_class == "warrior" or player_class == "Warrior":
        weapons = ["sword", "axe"]
        random_weapon = random.choice(weapons)
        print(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
    elif player_class == "ranger" or player_class == "Ranger":
        weapons = ["dagger", "bow"]
        random_weapon = random.choice(weapons)
        print(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
    else:
        weapons = ["staff", "spell tome"]
        random_weapon = random.choice(weapons)
        print(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)


def decision_3_b():
    """
    Outcome of the decision to remove the skeleton's armour. Offers
    choice of trying to find a weapon too.
    """
    worksheet_to_access = SHEET.worksheet("character")
    defense = worksheet_to_access.acell("J2").value
    final_defense = int(defense) + int(10)
    worksheet_to_access.update_cell(2, 10, int(final_defense))
    print(
        """
    While the armour isn't in the best shape it will protect you more than the
    ragged clothing you're currently wearing. As you remove the armour from
    the skeleton, it collapses in a heap on the floor. Unfortunately any
    chance of finding a weapon is now slim.
    """
    )
    print(
        """
    Would you like to try anyway?
    1. Yes.
    2. No, move on.
    3. Close your eyes again and wish for this game to end.
    """
    )

    while True:
        answer4 = input("")
        answers = ["1", "2", "3"]
        if answer4 in answers:
            print(f"You have chosen option {answer4}.")
        else:
            print("Please type either '1', '2', or '3'.")
            continue
        if answer4 == "1":
            luck = stat.roll_luck()
            if luck >= 30:
                wildcard(variables.player_class)
            else:
                print(
                    """
    You move the pile of rubble that was once the skeleton but fail to find
    anything of use.
    At least you have some armour now.
    """
                )
                stage_4()
        elif answer4 == "2":
            stage_4()
        else:
            exit_game()


def wildcard(player_class):
    """
    Function that plays if the player successfully rolls a high
    enough luck score to get a weapon as well as armour.
    """
    if player_class == "warrior" or player_class == "Warrior":
        weapons = ["sword", "axe"]
        random_weapon = random.choice(weapons)
        print(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
        stage_4()
    elif player_class == "ranger" or player_class == "Ranger":
        weapons = ["dagger", "bow"]
        random_weapon = random.choice(weapons)
        print(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
        stage_4()
    else:
        weapons = ["staff", "spell tome"]
        random_weapon = random.choice(weapons)
        print(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
        stage_4()


def preferred(weapon):
    """
    Function triggered if user obtains weapon. Checks
    to see if the weapon matches their preferred weapon
    and alters stats accordingly. Preferred weapon gets
    +15 attack, non preferred gets +5.
    """
    worksheet_to_pull = SHEET.worksheet("inventory")
    current_weapon = worksheet_to_pull.acell("B2").value
    if current_weapon == weapon:
        worksheet_to_access = SHEET.worksheet("character")
        attack = worksheet_to_access.acell("I2").value
        final_attack = int(attack) + int(15)
        worksheet_to_access.update_cell(2, 9, int(final_attack))
        print(f"Luckily you are skilled with a {current_weapon}!")
        print("This bodes well for any future fights.")
        stage_4()
    elif current_weapon != weapon:
        worksheet_to_access = SHEET.worksheet("character")
        attack = worksheet_to_access.acell("I2").value
        final_attack = int(attack) + int(5)
        worksheet_to_access.update_cell(2, 9, int(final_attack))
        print(
            """
        It may not be a weapon you're used to but you will still do better in
        a fight than if you were without it.
        """
        )
        stage_4()
    else:
        print("Game error.")


# Main event


def stage_4():
    """
    Scene 4 of the story and next decision.
    """
    print(
        """
    As you continue through the hallway, the lanterns get fewer and fewer, and
    with them the light gets dimmer and dimmer.
    """
    )
    worksheet_to_pull = SHEET.worksheet("inventory")
    inventory = worksheet_to_pull.col_values(1)
    if ("torch" or "lantern") in inventory:
        attack_him()
    else:
        noise()


def attack_him():
    print(
        """
    Thankfully you have your portable light source still and can see
    fairly clearly through the darkness. As you turn a corner, you take a sharp
    intake of breath and freeze. Just a few feet ahead of you is a very much
    reanimated skeleton; his bones creaking as they carry him up and down the
    hallway. You duck back behind the wall corner to decide on what to do next.
    """
    )
    print(
        """
            Do you...?
            1. Attack him preemptively before he notices you?
            2. Try to sneak past him?
            3. Close your eyes and wish for the game to end?
            """
    )
    while True:
        answer5 = input("")
        answers = ["1", "2", "3"]
        if answer5 in answers:
            print(f"You have chosen option {answer5}.")
        else:
            print("Please type either '1', '2', or '3'.")
            continue
        if answer5 == "1":
            attack = stat.roll_attack()
            if attack >= 30:
                print(
                    """
                        You make the decision to attack before you're noticed.
                        Thankfully, the skeleton remains unaware of your
                        presence and you strike him down with your weapon.
                        His bones fall to the floor with a clatter and all
                        is silent. It's safe to assume he's finished.
                        You're safe."""
                )
            else:
                dead()
        elif answer5 == "2":
            dex = stat.roll_dex()
            if dex >= 25:
                print(
                    """
                        You extinguish your light and quietly sneak around the
                        enemy, careful not to make too much noise. You're not
                        sure if the skeleton can still head without his flesh
                        ears but you don't want to take that chance.
                        Thankfully, you make it to the end of what you assume
                        is a corridor.
                        """
                )
                stage_5()
            else:
                print(
                    """
                        He sees you and it's too late. The last thing you
                        see is the glint of his sword coming towards you.
                        """
                )
                dead()
        else:
            exit_game()


def stage_5():
    """
    Scene 5 of the story and next decision.
    """
    print("Scene 5")


def dead():
    print("YOU HAVE DIED. GAME OVER")
    print(
        """
          Would you like to play again?
          1. Yes
          2. No
          """
    )
    answer = input("")
    answers = ["1", "2"]
    if answer in answers:
        print(f"You have chosen option {answer}.")
        if answer == "1":
            start_game()
        else:
            print("Thank you for playing.")
    else:
        print("Please type either '1', '2', or '3'.")
