import random
import time
import os
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


def typePrint(text):
    """
    Alters speed of text to mimic text being typed out.
    """
    text += "\n"
    for char in text:
        time.sleep(0.010)
        print(char, end="", flush=True)


# SCENE 1 POTENTIAL EVENTS


def wake_up():
    """
    Introduction for player, section 1 of the story.
    """
    typePrint(
        """
    You wake up in a cold, damp cave...
    You can't remember the last thing that happened to you, but here you are;
    Shivering...
    Confused...
    Lost...
    In the distance you can see a faint glow of light ahead of you.
    """
    )
    typePrint(
        """
    Do you...?
    1. Stand up and head directly towards the light despite being unable to
    see your surroundings?
    2. Feel around the area for any item that could be of use to you?
    3. Close your eyes again and wish for this game to end.
    """
    )

    typePrint("Please choose a option number\n")
    while True:
        answer1 = input("")
        answers = ["1", "2", "3"]
        if answer1 in answers:
            typePrint(
                f"You have chosen option {answer1}."
                " Let us see if the odds are in your favour..."
            )
        else:
            typePrint("Please type either '1', '2', or '3'.")
            continue
        return answer1


def exit_game():
    exit = """
    You close your eyes and fall asleep.
    The game is over. You will never know what could have been.
    Want to start again? Please type yes or no.
    """
    typePrint(exit)
    user_ans = input("")
    if user_ans == "Yes" or user_ans == "yes":
        start_game()
    elif user_ans == "No" or user_ans == "no":
        typePrint("GAME OVER. THANK YOU FOR PLAYING.")
    else:
        typePrint("Please type either yes/Yes or no/No")


def decision_one(answer1):
    """
    Generates outcome of first decision in game
    """
    if answer1 == "1":
        dex = stat.roll_dex()
        if dex >= 25:
            typePrint(
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
    typePrint(
        """
    Bang! You trip over something and land on your hands and knees. It's
    painful and although you can't see it, you can feel blood trickle down the
    palms of your hands.
    You lose 5 health points.
    """
    )
    typePrint(
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
            typePrint(
                f"You have chosen option {answer1}."
                " Let us see how you fare this time..."
            )
            decision_one(answer1)
        else:
            typePrint("Please type either '1', '2', or '3'.")
            continue
        return answer1


def fail_two():
    """
    Function that decides what happens
    should the player fail the second option
    of the first choice.
    """
    stat.update_hp(5)
    typePrint(
        """
    As you feel around, your hands meet the rough edge of the stone wall.
    'Success!' you think. Surely you can use this as a way to safely navigate
    to the exit. Instead, you cut open your hand on a sharp bit of rock jutting
    out from the wall.
    You lose 5 health points.
    """
    )
    typePrint(
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
            typePrint(
                f"You have chosen option {answer1}."
                " Let us see how you fare this time..."
            )
            decision_one(answer1)
        else:
            typePrint("Please type either '1', '2', or '3'.")
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
    os.system("clear")
    typePrint(
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
    os.system("clear")
    typePrint(
        """
    The source of the light is a iron lantern fixed to the wall.
    The cave seems to be starting to form into a carved out hallway with more
    lanterns lining the pathway down.
    """
    )

    worksheet_to_pull = SHEET.worksheet("inventory")
    inventory = worksheet_to_pull.col_values(1)
    if "torch" in inventory:
        typePrint(
            """
        You already have a light source thankfully, but the lanterns provide an
        extra bit of light for you. You continue down the corridor, following
        the more structured pathway.
        """
        )

        stage_3()
    else:
        typePrint(
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
                typePrint(
                    f"You have chosen option {answer2}."
                    " Let us see if the odds are in your favour..."
                )
                decision_two(answer2)
            else:
                typePrint("Please type either '1', '2', or '3'.")
                continue
            return answer2


def decision_two(answer2):
    """
    Generates outcome of second decision in game
    """
    if answer2 == "1":
        strength = stat.roll_strength()
        if strength >= 25:
            os.system("clear")
            typePrint(
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
        typePrint(
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
    os.system("clear")
    typePrint(
        """
    The lantern is wedged into the wall much deeper than you expected. You put
    all your strength into it and pull but unfortunately one of your hands
    slips and crushes the glass inside the lantern. Shards of glass and hot
    candle wax cover your hand, burning and cutting it.
    You lose 10 health points.
    """
    )
    typePrint(
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
            typePrint(f"You have chosen option {answer2}.")
            if answer2 == "1":
                stage_3()
            else:
                exit_game()
        else:
            typePrint("Please type either '1' or '2'")
            continue
        return answer2


# END OF SCENE 2 EVENTS

# SCENE 3 POTENTIAL EVENTS

# Main event


def stage_3():
    """
    Scene 3 of the story and next decision.
    """
    os.system("clear")
    typePrint(
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
    typePrint(
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
            typePrint(f"You have chosen option {answer3}.")
        else:
            typePrint("Please type either '1', '2', or '3'.")
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
    os.system("clear")
    typePrint(
        """
    You shove the skeleton over to check underneath him for a weapon.
    Unfortunately he is heavier than he looks and the weight of his armour
    and bones causes the straps of his armour to snap. While that now may be
    unusable, you've thankfully found a weapon.
    """
    )
    if player_class == "warrior" or player_class == "Warrior":
        weapons = ["sword", "axe"]
        random_weapon = random.choice(weapons)
        typePrint(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
    elif player_class == "ranger" or player_class == "Ranger":
        weapons = ["dagger", "bow"]
        random_weapon = random.choice(weapons)
        typePrint(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
    else:
        weapons = ["staff", "spell tome"]
        random_weapon = random.choice(weapons)
        typePrint(f"You have found a {random_weapon}!")
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
    os.system("clear")
    typePrint(
        """
    While the armour isn't in the best shape it will protect you more than the
    ragged clothing you're currently wearing. As you remove the armour from
    the skeleton, it collapses in a heap on the floor. Unfortunately any
    chance of finding a weapon is now slim.
    """
    )
    typePrint(
        """
    Would you like to try anyway?
    1. Yes.
    2. No, move on.
    3. Close your eyes again and wish for this game to end.
    Please choose a option number.
    """
    )

    while True:
        answer4 = input("")
        answers = ["1", "2", "3"]
        if answer4 in answers:
            typePrint(f"You have chosen option {answer4}.")
        else:
            typePrint("Please type either '1', '2', or '3'.")
            continue
        if answer4 == "1":
            luck = stat.roll_luck()
            if luck >= 30:
                wildcard(variables.player_class)
            else:
                typePrint(
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
        typePrint(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
        stage_4()
    elif player_class == "ranger" or player_class == "Ranger":
        weapons = ["dagger", "bow"]
        random_weapon = random.choice(weapons)
        typePrint(f"You have found a {random_weapon}!")
        worksheet_to_update = SHEET.worksheet("inventory")
        worksheet_to_update.update_cell(2, 2, random_weapon)
        preferred(variables.weapon)
        stage_4()
    else:
        weapons = ["staff", "spell tome"]
        random_weapon = random.choice(weapons)
        typePrint(f"You have found a {random_weapon}!")
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
        typePrint(f"Luckily you are skilled with a {current_weapon}!")
        typePrint("This bodes well for any future fights.")
        stage_4()
    elif current_weapon != weapon:
        worksheet_to_access = SHEET.worksheet("character")
        attack = worksheet_to_access.acell("I2").value
        final_attack = int(attack) + int(5)
        worksheet_to_access.update_cell(2, 9, int(final_attack))
        typePrint(
            """
        It may not be a weapon you're used to but you will still do better in
        a fight than if you were without it.
        """
        )
        stage_4()
    else:
        typePrint("Game error.")


# END OF SCENE 3 EVENTS

# SCENE 4 POTENTIAL EVENTS

# Main event


def stage_4():
    """
    Scene 4 of the story and next decision.
    """

    typePrint(
        """
    As you continue through the hallway, the lanterns get fewer and fewer, and
    with them the light gets dimmer and dimmer.
    """
    )
    worksheet_to_pull = SHEET.worksheet("inventory")
    inventory = worksheet_to_pull.col_values(1)
    if "torch" in inventory:
        attack_him()
    elif "lantern" in inventory:
        attack_him()
    else:
        noise()


def attack_him():
    """
    Function triggered if player has a light source. Allows them to attack or
    try sneak past the enemy.
    """

    typePrint(
        """
    Thankfully you have your portable light source still and can see
    fairly clearly through the darkness. As you turn a corner, you take a sharp
    intake of breath and freeze. Just a few feet ahead of you is a very much
    reanimated skeleton; his bones creaking as they carry him up and down the
    hallway. You duck back behind the wall corner to decide on what to do next.
    """
    )
    typePrint(
        """
            Do you...?
            1. Attack him preemptively before he notices you?
            2. Try to sneak past him?
            3. Close your eyes and wish for the game to end?
            Please choose a option number.
            """
    )
    while True:
        answer5 = input("")
        answers = ["1", "2", "3"]
        if answer5 in answers:
            typePrint(f"You have chosen option {answer5}.")
        else:
            typePrint("Please type either '1', '2', or '3'.")
            continue
        if answer5 == "1":
            attack = stat.roll_attack()
            if attack >= 30:
                typePrint(
                    """
                        You make the decision to attack before you're noticed.
                        Thankfully, the skeleton remains unaware of your
                        presence and you strike him down with your weapon.
                        His bones fall to the floor with a clatter and all
                        is silent. It's safe to assume he's finished.
                        You're safe."""
                )
                stage_5()
            else:
                typePrint(
                    """
                        He sees you and it's too late. The last thing you
                        see is the glint of his sword coming towards you.
                        """
                )
                dead()
        elif answer5 == "2":
            dex = stat.roll_dex()
            if dex >= 25:
                typePrint(
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
                typePrint(
                    """
                        He sees you and it's too late. The last thing you
                        see is the glint of his sword coming towards you.
                        """
                )
                dead()
        else:
            exit_game()


def noise():
    """
    Triggered if player has no light source and does not see the enemy. Rolls
    dex & luck, if successful player lives, if not, player dies.
    """

    typePrint(
        """
        As you come around a corner, you hear a noise. It's a strange creaking
        sound, like teeth grinding against each other. You freeze as you try
        to figure out what next to do. Before you can even taken another
        breath, you hear the sound of metal whirling through the air towards
        you.
        """
    )
    dex = stat.roll_dex()
    luck = stat.roll_luck()
    survival = int(dex) + int(luck)
    if survival >= 60:
        typePrint(
            """
            Someone was looking out for you today. Although you can't even see
            what you're dodging, you manage to move out of the way of the
            weapon that was hurtling towards you and you hear it embed it's
            blade into the dirt ground. You almost trip in the dark but find
            your footing when your shoulder collides with a wall. Not sure
            where the enemy is, you have no choice but to run forward in
            the dark. There is more light ahead and your enemy seems
            preoccupied attempting to dislodge his weapon from the ground.
            Somehow, you make it.
            """
        )
        stage_5()
    else:
        typePrint(
            """
            Your enemy strikes you. The last thing you see as you fall to the
            ground is the skeleton's glowing red eyes.
            """
        )
        dead()


# END OF SCENE 4 EVENTS

# SCENE 5 POTENTIAL EVENTS

# Main event


def stage_5():
    """
    Scene 5 of the story and next decision.
    """
    typePrint(
        """
        At the end of the corridor is a iron gate. To ensure nothing follows
        you into the next room, you decide it is best to pull the chain and
        close the gate behind you as you move forwards.
        """
    )
    typePrint(
        """
    The next room is almost like a dome. Torches are lit all along the walls
    and aside from what look like some sealed closed urns, there's little else
    there other than a great big stone door and a pedestal in front of it.
    You approach the pedestal and resting on top of it, you find an old looking
    box. There's what looks like a crudely made keyhole on the front of it.
    """
    )
    worksheet_to_pull = SHEET.worksheet("inventory")
    inventory = worksheet_to_pull.col_values(1)
    if ("key") in inventory:
        unlock()
    else:
        mini_game()


def unlock():
    typePrint(
        """
    You remember the key you found when you first woke up. Perhaps...?
    You take out the rusted key a slide it into the box's keyhole and turn. To
    your delight, there is a loud click and the box opens. You're not sure what
    to expect since the box is so plain looking, but the contents do catch you
    by surprise.
    Inside is a small stone tablet with fairly simplistic etchings of a bird,
    a frog and a wolf. This doesn't exactly make sense to you until you look up
    at the giant stone door in front of you. It looks set in place with no way
    of moving it, but in the centre are three small icons.
    """
    )
    typePrint(
        """
        Upon further inspection, you see that these icons match those on the
        stone tablet you've just acquired, but are in a different order. You
        run your fingers over the icons and are surprised to see that they can
        be moved. Perhaps moving them into the same order as is on the tablet
        will prompt the door to open?
        """
    )
    typePrint(
        """
    Do you...?
    1. Move the icons to the order shown on the tablet?
    2. Close your eyes and wish for the game to end?
    Please choose a option number.
    """
    )
    while True:
        answer = input("")
        answers = ["1", "2"]
        if answer in answers:
            typePrint(f"You have chosen option {answer}.")
        else:
            typePrint("Please type either '1', '2', or '3'.")
            continue
        if answer == "1":
            freedom()
        else:
            exit_game()


def mini_game():
    """
    Triggers if player does not have a key and must therefore guess the correct
    order of the icons. Relies on luck stat rolls.
    """
    typePrint(
        """
    There doesn't seem to be any other way to open the box and you are without
    a key, so you are forced to look for another solution. Something on the
    large door in front of you catches your eye as you glance around. It looks
    set in place with no way of moving it, but in the centre are three small
    icons in the shape of a frog, a bird and a wolf. You run your fingers over
    the icons and are surprised to see that they can be moved. Perhaps moving
    them into a certain order will prompt the door to open?
    """
    )
    typePrint(
        """
    Do you...?
    1. Move the icons and hope the order you've chosen is correct?
    2. Close your eyes and wish for the game to end?
    Please choose a option number.
    """
    )
    while True:
        answer = input("")
        answers = ["1", "2"]
        if answer in answers:
            typePrint(f"You have chosen option {answer}.")
        else:
            typePrint("Please type either '1', '2', or '3'.")
            continue
        if answer == "1":
            luck = stat.roll_luck()
            if luck >= 29:
                freedom()
            else:
                luck_fail()
        else:
            exit_game()


def luck_fail():
    typePrint(
        """
    You hold your breath as the icons slide into place and wait for something
    to happen. There is nothing but silence. The door didn't open, but neither
    did anything bad happen.
    Would you like to try again?
    1. Try again.
    2. Close your eyes and wish for the game to end?
    Please choose a option number.
    """
    )
    while True:
        answer = input("")
        answers = ["1", "2"]
        if answer in answers:
            typePrint(f"You have chosen option {answer}.")
        else:
            typePrint("Please type either '1' or '2'")
            continue
        if answer == "1":
            luck = stat.roll_luck()
            if luck >= 29:
                freedom()
            else:
                luck_fail2()
        else:
            exit_game()


def luck_fail2():
    typePrint(
        """
    Your heart pounds as you try another combination. There is a split second
    between the icons sliding into place and a hissing sound. All you feel is
    burning pain as arrows shoot from hidden slots in the walls. One hits you
    and it is obviously dipped in poison if the pain is anything to go by.
    You lose 20HP.
    Do you...?
    1. Try again?
    2. Close your eyes and wish for the game to end?
    Please choose a option number.
    """
    )
    stat.update_hp(20)
    while True:
        answer = input("")
        answers = ["1", "2"]
        if answer in answers:
            typePrint(f"You have chosen option {answer}.")
        else:
            typePrint("Please type either '1' or '2'")
            continue
        if answer == "1":
            luck = stat.roll_luck()
            if luck >= 29:
                freedom()
            else:
                typePrint(
                    """
                    As the icons slide into place once again, you close your
                    eyes and pray you were right this time. While no more
                    arrows shoot out, you hear the gate you closed behind you
                    earlier open and the creaking of a skeleton approach. You
                    are gravely injured from the poisoned arrow. You can't
                    fight back this time.
                    """
                )
                dead()
        else:
            exit_game()


def freedom():
    typePrint(
        """
    Everything is still for a moment and you fear you've made a mistake until
    suddenly there's a grinding sound and the door begins to lift. Dust flies
    everywhere and the bright light of sunlight begins to spill into the room.
    You shield your eyes from the dust and light as the door continues to open,
    until finally, you feel fresh air on your face.
    You are free.
    """
    )
    congrats()


# END OF SCENE 5 EVENTS

# Misc functions


def congrats():
    typePrint(
        """
        Congratulations! You've escapes the cave! Thank you for playing. Would
        you like to try again?
        1. Yes
        2. No
        """
    )
    while True:
        answer = input("")
        answers = ["1", "2"]
        if answer in answers:
            typePrint(f"You have chosen option {answer}.")
        else:
            typePrint("Please type either '1' or '2'")
            continue
        if answer == "1":
            start_game()
        else:
            typePrint("Thank you again for playing!")


def dead():
    """
    Triggered if player is killed by an enemy. Gives option to retry game.
    """
    typePrint("YOU HAVE DIED. GAME OVER")
    typePrint(
        """
        Would you like to play again?
        1. Yes
        2. No
        """
    )
    answer = input("")
    answers = ["1", "2"]
    if answer in answers:
        typePrint(f"You have chosen option {answer}.")
        if answer == "1":
            start_game()
        else:
            typePrint("Thank you for playing.")
    else:
        typePrint("Please type either '1', '2', or '3'.")
