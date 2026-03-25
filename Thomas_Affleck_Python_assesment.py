# Libraries
import random
import time
#import keyboard

# Global variables
materials = ["stone", "copper", "steel", "steel", "steel", "copper"] # Need to either make a dictionary with type and quantity or store multiple copies of same thing and then check over it to see how many in inventory.
used_materials = []
fuel_value = 50
ship_fuel = 0
ship_broken = True
fuel_in_ship = 0
TEXT_SLEEP_TIME = 0.1
LINE_SLEEP_TIME = 0.5
FUEL_DELAY = 1
hints = 5


# Functions
def slow_type(sentence):  # Function to enable typewriter style typing.
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(TEXT_SLEEP_TIME)
    print()


def start_menu():  # Menu to run at start, need to add function to restart whenever r key pressed.
    global name
    slow_type("You are stuck on the planet Blam")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("Your ship is broken down.")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("You will have to fix your ship first and then make your way back to Earth, fueling and fixing your ship along the way.")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("Any challenges you face along the way will be explained to you.")
    while True:
        try:
            choice = int(input("Press 1 to play or 2 to quit "))
            if choice == 1:
                break
            elif choice == 2:
                quit()
            else:
                print("That's not the right number")
        except ValueError:
            print("That's not a number")
    name = input("What is your name? ")
    print(f"Your name is {name}")
    game_menu()


def game_menu():
    global ship_broken
    global fuel_in_ship
    if ship_broken == False and fuel_in_ship < 20:
        while True:
            try:
                print("Press 1 to fuel your ship")
                choice2 = int(input())
                if choice2 == 1:
                    fuel()
                    break
                else:
                    print("That's not the right number")
            except ValueError:
                print("That's not a number")
    else:
        while True:
            try:
                print()
                print(
                    "To fix your ship you need to use 3 steel, 2 copper and 1 stone. You will also need to find at least 20 units of fuel to put into your ship.")
                print()
                print("Press 1 to go find materials to fix your ship. Press 2 to work on your ship. Press 3 to fuel your ship.")
                choice = int(input())
                if choice == 1:
                    explore()
                    break
                elif choice == 2:
                    garage()
                    break
                elif choice == 3:
                    fuel()
                    break
                else:
                    print("That's not the right number")
            except ValueError:
                print("That's not a number")


def explore(): # Maybe similar to the pokemon game, going between areas? Could do word puzzles when in an area???
    print("Explore")


def garage():  # Make it so you also get fuel from this option, possibly raw oil to refine?? Need to decide how to run search for materials too, might design different areas...
    global materials # Function done? Think so...
    global used_materials
    global ship_broken
    if len(materials) == 0:
        print("You have no materials! Returning to menu")
        game_menu()
    else:
        while True:
            try:
                print("In your inventory you have:")
                for item in materials:
                    print(item)
                print("Please type what material you want to use:")
                materials_to_use = input().lower()
                if materials_to_use not in materials:
                    print("You don't have those materials.")
                else:
                    break
            except ValueError:
                print("That's not right")

        while True:
            try:
                print(f"How many of {materials_to_use} do you want to use?")
                quantity_materials_use = int(input())
                materials_count = materials.count(materials_to_use)
                if quantity_materials_use > materials_count:  # Need to ensure that it checks the correct spot in the list for the quantity, should work now.
                    print("You don't have enough of those!")
                elif quantity_materials_use <= 0:
                    print("That's not the right number!")
                else:
                    print(f"You want to use {quantity_materials_use} {materials_to_use}.")
                    print()
                    print("Applying materials...")
                    for i in range(quantity_materials_use): # Adding used materials to used materials list, so it can check if player has applied all the correct materials to ship.
                        used_materials.append(materials_to_use) # Might be not needed with thing below. Needed...
                        materials.remove(materials_to_use)
                    print(used_materials) # Temp to ensure items added to used list
                    if used_materials.count("steel") == 3 and used_materials.count("copper") == 2 and used_materials.count("stone") == 1:#3 steel, 2 copper, 1 stone
                        print("You have fixed your ship!")
                        ship_broken = False
                        game_menu()
                        break
                    else:
                        game_menu()
                        break
            except ValueError:
                print("That's not right")


def fuel(): # Player to select how much fuel to put into ship, links to a function at the end if ship is fueled and fixed, otherwise returns to menu
    global ship_broken  # Function done?
    global fuel_value
    global fuel_in_ship
    if fuel_value <= 0:  # Checks to see if player has fuel to put in ship
        print("You have no fuel! Returning to menu")
        game_menu()
    else:  # If player has fuel
        print(f"You have {fuel_value} units of fuel")
        while True:
            try:
                print("Type a number for how much fuel you want to put in your ship")
                fuel_into_ship = int(input())
                if fuel_into_ship > fuel_value:
                    print("You don't have that much fuel!")
                elif fuel_into_ship <= 0:
                    print("That's not the right number!")
                else:
                    print(f"Putting {fuel_into_ship} units of fuel into ship...")
                    time.sleep(FUEL_DELAY)
                    fuel_in_ship = fuel_in_ship + fuel_into_ship
                    print(f"Your ship now has {fuel_in_ship} units of fuel in it")
                    fuel_value = fuel_value - fuel_into_ship
                    break
            except ValueError:
                print("That's not a number!")
        if fuel_in_ship >= 20 and ship_broken == False: # If player meets criteria of 20 units of fuel and fixed ship then go to take off.
            take_off()
        elif fuel_in_ship >= 20 and ship_broken == True: # If player has enough fuel but broken ship
            print("Your ship is fueled but not fixed! Returning to menu.")
            game_menu()
        elif fuel_in_ship < 20 and ship_broken == False: # If player has fixed ship but not enough fuel
            print("Your ship is fixed but you don't have enough fuel to take off! You need at least 20 units in your ship to take off. Find some more and then come back!")
            print()
            game_menu()
        elif fuel_in_ship < 20 and ship_broken == True: # If player doesn't meet either of the criteria to take off
            print("Your ship is still broken and you don't have enough fuel to take off! Go fix your ship and then put in at least 20 units of fuel to take off.")
            print()
            game_menu()


def take_off():
    print("You have fixed your ship and are now ready to take off!")
    while True:
        try:
            print("Press the w key to take off")
            choice = input().lower()
            if choice == "w":
                print("TAKE OFF!!!")
                in_space()
                break
            else:
                print("How'd you mess that up?")
        except ValueError:
            print("How'd you mess that up?")

def in_space():
    print("In space")
    print("Please pick what planet you want to go to")
    planet_choice = input()


# Main
#start_menu()
take_off()


#Testing/addition zone:

#materials_count = materials.count("Stone")
#print(materials_count)
#materials.remove(materials_to_use)

