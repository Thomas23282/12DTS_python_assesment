# Libraries
import random
import time

# Global variables
materials = []
fuel_value = 0
ship_fuel = 0
ship_broken = True
TEXT_SLEEP_TIME = 0.1
LINE_SLEEP_TIME = 0.5
hints = 5


# Functions
def slow_type(sentence):  # Function to enable typewriter style typing.
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(TEXT_SLEEP_TIME)
    print()


def start_menu():  # Menu to run at start, need too add function to restart whenever r key pressed.
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
    if ship_broken == False and fuel_value > 0:
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


def explore():
    print("Explore")


def garage():  # Make it so you also get fuel from this option, possibly raw oil to refine?? Need to decide how to run search for materials too, might design different areas...
    global materials
    if len(materials) == 0:
        print("You have no materials! Returning to menu")
        game_menu()
    else:
        print(f"You have {materials} in your inventory")


def fuel():
    global fuel_value
    if fuel_value <= 0:
        print("You have no fuel! Returning to menu")
        game_menu()
    else:
        print(f"You have {fuel_value} units of fuel")
        print("Type a number for how much fuel you want to put in your ship")


# Main
start_menu()
# explore()
