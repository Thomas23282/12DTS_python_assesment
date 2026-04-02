# Libraries
import random
import time
#import keyboard

# Global variables
materials = [] # Need to either make a dictionary with type and quantity or store multiple copies of same thing and then check over it to see how many in inventory.
used_materials = []
planets = ["Blam", "Axiom", "Delta Majora", "Earth"] # Planet names so function can be reused
fuel_value = 0 # Fuel in player inventory
ship_fuel = 0
ship_broken = True
fuel_in_ship = 0
TEXT_SLEEP_TIME = 0.1
LINE_SLEEP_TIME = 0.5
MATERIAL_SLEEP_TIME = 1
FUEL_DELAY = 1
planet_name = 0
hints = 5
name = 0
areas = ["Metal field", "Copper cave", "Stony plains"]
ship_parts = {"engine": "ok", "hull": "ok", "navigation": "ok"} # Which part of the ship can break later
fuel_used = [15,20,25] #  Different fuel amounts to use to travel to different planets
planet_index = 0
planet_name = planets[planet_index]


# Functions
def restart(): # Resets all variables that have been changed in gameplay
    global name
    global ship_broken
    global fuel_in_ship
    global materials
    global fuel_value
    global used_materials
    global ship_parts
    global planet_index
    name = 0
    ship_broken = True
    fuel_in_ship = 0
    materials = []
    fuel_value = 0
    used_materials = []
    ship_parts = {"engine": "ok", "hull": "ok", "navigation": "ok"}
    planet_index = 0
    start_menu()


def show_progress():
    global used_materials
    global planet_name
    print("Repair progress:")
    print("Steel:", used_materials.count("steel"), "/ 3")
    print("Copper:", used_materials.count("copper"), "/ 2")
    print("Stone:", used_materials.count("stone"), "/ 1")
    if planet_name == "Blam":
        game_menu()
    elif planet_name == "Axiom" or planet_name == "Delta Majora":
        planet()

def slow_type(sentence):  # Function to enable typewriter style typing.
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(TEXT_SLEEP_TIME)
    print()

def word_puzzle(word): # Takes word input, scrambles it and gives it to player to solve, then returns true or false
    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)

    print("Unscramble this word:")
    print(scrambled_word)
    guess = input("Answer: ").lower()

    if guess == word:
        print("Correct")
        return True
    else:
        print("Wrong")
        return False

def start_menu():  # Menu to run at start, need to add function to restart whenever r key pressed.
    global title_name
    global planet_name
    planet_name = planets[0]
    slow_type("You are stuck on the planet Blam")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("Your ship is broken down.")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("You will have to fix your ship first and then make your way back to Earth, fueling and fixing your ship along the way.")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("Any challenges you face along the way will be explained to you.")
    time.sleep(LINE_SLEEP_TIME)
    slow_type("You will get fuel when you gather materials.")
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
    while True:
        try:
            name = input("What is your name? ")
            if name.isalpha(): # Checks if any numbers in name
                title_name = name.title()
                print(f"Your name is {title_name}")
                game_menu()
            else:
                print("That doesn't look like a name...")
        except ValueError:
            print("That doesn't look like a name... ")


def game_menu():
    global ship_broken
    global fuel_in_ship
    global fuel_value
    if ship_broken == False and fuel_in_ship < 20: # Goes this way if ship is fixed but not fueled
        while True:
            try:
                print("Press 1 to fuel your ship or 2 to get more fuel")
                choice2 = int(input())
                if choice2 == 1:
                    fuel_menu()
                    break
                elif choice2 == 2:
                    material = "fuel"
                    if word_puzzle(material): # Checks if player completes word puzzle
                        fuel = random.randint(3,7) # Picks a random amount of fuel to give player
                        fuel_value += fuel
                        print(f"You found {fuel} units of fuel")
                        time.sleep(MATERIAL_SLEEP_TIME)
                else:
                    print("That's not the right number")
            except ValueError:
                print("That's not a number")
    else:
        print("To fix your ship you need to use 3 steel, 2 copper and 1 stone. You will also need to find at least 20 units of fuel to put into your ship.")
        while True:
            try:
                print()
                print("Press 1 to go find materials to fix your ship. Press 2 to work on your ship. Press 3 to fuel your ship. Press 4 to restart")
                choice = int(input())
                if choice == 1:
                    explore()
                    break
                elif choice == 2:
                    garage()
                    break
                elif choice == 3:
                    fuel_menu()
                    break
                elif choice == 4:
                    restart()
                    break
                else:
                    print("That's not the right number")
            except ValueError:
                print("That's not a number")


def explore(): # Players pick an area and solve a word puzzle for materials and fuel
    global materials
    global fuel_value
    global planet_name
    print()
    while True:
        try:
            print("Where do you want to explore?")
            print("1: Metal field")
            print("2: Copper cave")
            print("3: Stony plains")
            print("4: Restart game")
            choice = int(input())
            if choice == 1:
                material = "steel"
                break
            elif choice == 2:
                material = "copper"
                break
            elif choice == 3:
                material = "stone"
                break
            elif choice == 4:
                restart()
                break
            else:
                print("That's not a place")
                game_menu()
                break
        except ValueError:
            print("That's not a number")

    print("You explore the area...")
    if word_puzzle(material):
        amount = random.randint(1,3)
        for i in range(amount):
            materials.append(material)
        print(f"You found {amount} {material}")
        time.sleep(MATERIAL_SLEEP_TIME)
        fuel = random.randint(3,7) # Gives player random amount of fuel between 3 and 7, might make it give more, to make it not take so long
        fuel_value += fuel
        print(f"You found {fuel} units of fuel")
        time.sleep(MATERIAL_SLEEP_TIME)

    if planet_name == "Blam": # Decides which function to send player back to
        game_menu()
    elif planet_name == "Axiom" or planet_name == "Delta Majora":
        planet()



def garage():  # Where player fixes ship
    global materials # Function done? Think so...
    global used_materials
    global ship_broken
    global steel_count
    global copper_count
    global stone_count

    steel_count = materials.count("steel") # Counting how many of each item player has to display
    copper_count = materials.count("copper")
    stone_count = materials.count("stone")
    if len(materials) == 0 and len(used_materials) == 0:
        slow_type("You need to find some materials before you can use them on your ship!")
        game_menu()
    else:
        while True:
            try:
                print("Press 1 to use materials")
                print("Press 2 to see materials applied to ship")
                print("Press 3 to go back")
                print("Press 4 to restart")
                choice = int(input())
                if choice == 1:
                    while True:
                        try:
                            print("In your inventory you have:")
                            print(f"Steel: {steel_count}")
                            print(f"Copper: {copper_count}")
                            print(f"Stone: {stone_count}")
                            print("Please type what material you want to use, or type back to go back to the menu:") # Gives player option to go back and not get stuck here
                            materials_to_use = input().lower()
                            if materials_to_use == "back":
                                game_menu()
                            elif materials_to_use not in materials:
                                print("You don't have those materials.")
                            else:
                                break
                        except ValueError:
                            print("That's not right")

                    while True:
                        try:
                            print(f"How many of {materials_to_use} do you want to use, or type 0 to return to menu.")
                            quantity_materials_use = int(input())
                            materials_count = materials.count(materials_to_use)
                            if quantity_materials_use == 0:
                                game_menu()
                                break
                            elif quantity_materials_use > materials_count:  # Checks if player has enough of material
                                print("You don't have enough of those!")
                            elif quantity_materials_use <= 0:
                                print("That's not the right number!")
                            else:
                                print(f"You want to use {quantity_materials_use} {materials_to_use}.")
                                print()
                                print("Applying materials...")
                                for i in range(quantity_materials_use): # Adding used materials to used materials list, so it can check if player has applied all the correct materials to ship.
                                    used_materials.append(materials_to_use) #
                                    materials.remove(materials_to_use)
                                if used_materials.count("steel") >= 3 and used_materials.count("copper") >= 2 and used_materials.count("stone") >= 1:#3 steel, 2 copper, 1 stone
                                    print("You have fixed your ship!")
                                    ship_broken = False
                                    game_menu()
                                    break
                                else:
                                    game_menu()
                                    break
                        except ValueError:
                            print("That's not right")

                elif choice == 2:
                    if len(used_materials) == 0:
                        print("You've not used any materials")
                    else:
                        show_progress()
                elif choice == 3:
                    game_menu()
                    break
                elif choice == 4:
                    restart()
                    break
            except ValueError:
                print("That's not a number")

def fuel_menu(): # Player to select how much fuel to put into ship, links to a function at the end if ship is fueled and fixed, otherwise returns to menu
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
                print("Type a number for how much fuel you want to put in your ship, or type 0 to return")
                fuel_into_ship = int(input())
                if fuel_into_ship == 0:
                    game_menu()
                    break
                elif fuel_into_ship > fuel_value: # If player is trying to put in more than they have
                    print("You don't have that much fuel!")
                elif fuel_into_ship < 0:
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
    if ship_broken == True: # If player hasn't fixed the ship on further planets
        print("Your ship is still broken, you can't take off!")
        return
    slow_type("Your ship systems are coming back online...")
    time.sleep(1)
    while True:
        try:
            print("Press the W key to take off or R to restart")
            choice = input().lower()
            if choice == "w":
                slow_type("TAKE OFF!!!")
                in_space()
                break
            elif choice == "r":
                restart()
                break
            else:
                print("How'd you mess that up?")
        except ValueError:
            print("How'd you mess that up?")

def in_space(): # When player has taken off.
    global planets
    global planet_name
    global fuel_in_ship
    global fuel_used
    global ship_broken
    global used_materials
    global ship_parts
    global planet_index

    print("You are in space")
    next_index = planet_index + 1 # Moving forward on the list of planet names
    next_planet = planets[next_index] # Calling the next planet name
    fuel_cost = fuel_used[planet_index] # Uses the amount of fuel linked to travelling to that planet
    print(f"You are travelling to {next_planet}")
    print(f"It will cost {fuel_cost} units of fuel")
    if fuel_in_ship < fuel_cost: # If player tries to travel to final planet with not enough fuel
        lose_game()
        return
    else:
        fuel_in_ship -= fuel_cost
        slow_type("Travelling...")
        time.sleep(1)
        planet_index += 1
        planet_name = planets[planet_index] # Gets planet name from list
        if planet_name == "Earth":
            win_game()
            return
        else:
            random_chance = random.randint(1,3) # Random chance whether the ship breaks or not
            if random_chance == 1:
                random.shuffle(used_materials)
                mat1 = random.randint(0,len(used_materials)-1) # Remove one random material from ship
                used_materials.pop(mat1)
                mat2 = random.randint(0,len(used_materials)-1) # Same as above again
                used_materials.pop(mat2)
                ship_broken = True # Sets ship to broken so can't take off
                part = random.choice(["engine", "hull", "navigation"])  # Picks a random part to break
                ship_parts[part] = "broken" # Sets the random chosen part to broken
                slow_type("Your landing was rough...")
                for part in ship_parts: # Prints out ship parts statuses
                    print(part, ":", ship_parts[part])
            slow_type(f"You landed on {planet_name}")
            planet()


def planet(): # When on next two planets
    global planet_name
    global fuel_in_ship
    global fuel_value
    global ship_parts
    global fuel_used
    global used_materials
    global materials
    global ship_broken

    slow_type(f"You are now on the planet {planet_name}")
    print(f"You have {fuel_in_ship} units of fuel left in your ship")
    print(f"You have {fuel_value} units of fuel")


    print()
    slow_type("What would you like to do?")
    while True:
        try:
            print("1 Explore the planet")
            print("2 Check ship status")
            print("3 Fix ship")
            print("4 Fuel ship")
            print("5 Continue journey")
            print("6 Restart")

            choice = int(input())
            if choice == 1:
                explore()
                break
            elif choice == 2:
                print()
                print("--Ship status--")
                print(f"Planet: {planet_name}")
                print(f"Fuel remaining in ship: {fuel_in_ship}")
                print(f"Fuel in inventory: {fuel_value}")
                print("Materials:")
                print(f"Steel: {materials.count('steel')}")
                print(f"Copper: {materials.count('copper')}")
                print(f"Stone: {materials.count('stone')}")
                show_progress() # Shows what materials on the ship broke and need replaced

                print()

            elif choice == 3:
                planet_garage()
                break

            elif choice == 4:
                planet_fuel_menu()
                break

            elif choice == 5:
                next_planet()
                break

            elif choice == 6:
                restart()
                break

            else:
                print("That's not the right number")
        except ValueError:
            print("That's not a number")




def lose_game(): # When you lose
    slow_type("You are stuck in space")
    slow_type("You lose...")
    slow_type("The game will restart in 10 seconds or press r to restart now")
    while True:
            choice = input().lower()
            if choice == "r":
                restart()
                break
            else: # Restarts after 10 seconds
                time.sleep(10)
                restart()
                break

def win_game(): # When you win
    slow_type("Congrats you made it back to earth!")
    slow_type("You win!!!")
    slow_type("The game will restart in 10 seconds or press r to restart now")
    while True:
            choice = input().lower()
            if choice == "r":
                restart()
                break
            else: # Restarts after 10 seconds
                time.sleep(10)
                restart()
                break

def next_planet(): # When player tries to move to next planet
    global ship_broken
    global fuel_in_ship
    global fuel_value
    global fuel_used

    if ship_broken == True: # If player hasn't fixed ship
        print("Your ship is still damaged, you need to fix it before taking off")
        planet()
        return
    if fuel_in_ship < 20: # If player hasn't fueled ship
        print("You need to fuel your ship before travelling")
        planet()
        return
    take_off() # If player meets both criteria



def planet_garage(): # Same as earlier garage but links back to planet()
    global materials
    global used_materials
    global ship_broken
    global steel_count
    global copper_count
    global stone_count
    steel_count = materials.count("steel")
    copper_count = materials.count("copper")
    stone_count = materials.count("stone")
    while True:
        try:
            print("In your inventory you have:")
            print(f"Steel: {steel_count}")
            print(f"Copper: {copper_count}")
            print(f"Stone: {stone_count}")
            print("Please type what material you want to use, or type back to go back to the menu:")
            materials_to_use = input().lower()
            if materials_to_use == "back":
                planet()
            elif materials_to_use not in materials:
                print("You don't have those materials.")
            else:
                break
        except ValueError:
            print("That's not right")

    while True:
        try:
            print(f"How many of {materials_to_use} do you want to use, or type 0 to return to menu.")
            quantity_materials_use = int(input())
            materials_count = materials.count(materials_to_use)
            if quantity_materials_use == 0:
                planet()
                break
            elif quantity_materials_use > materials_count:  # Need to ensure that it checks the correct spot in the list for the quantity, should work now.
                print("You don't have enough of those!")
            elif quantity_materials_use <= 0:
                print("That's not the right number!")
            else:
                print(f"You want to use {quantity_materials_use} {materials_to_use}.")
                print()
                print("Applying materials...")
                for i in range(quantity_materials_use):  # Adding used materials to used materials list, so it can check if player has applied all the correct materials to ship.
                    used_materials.append(materials_to_use)  # Might be not needed with thing below. Needed...
                    materials.remove(materials_to_use)
                if used_materials.count("steel") >= 3 and used_materials.count("copper") >= 2 and used_materials.count("stone") >= 1:  # 3 steel, 2 copper, 1 stone
                    print("You have fixed your ship!")
                    ship_broken = False
                    planet()
                    break
                else:
                    planet()
                    break
        except ValueError:
            print("That's not right")

def planet_fuel_menu(): # If player picks to fuel ship when on later planets
    global ship_broken
    global fuel_value
    global fuel_in_ship
    if fuel_value <= 0:  # Checks to see if player has fuel to put in ship
        print("You have no fuel! Returning to menu")
        planet()
    else:  # If player has fuel
        print(f"You have {fuel_value} units of fuel")
        while True:
            try:
                print("Type a number for how much fuel you want to put in your ship, or type 0 to return")
                fuel_into_ship = int(input())
                if fuel_into_ship == 0:
                    planet()
                    break
                elif fuel_into_ship > fuel_value:
                    print("You don't have that much fuel!")
                elif fuel_into_ship < 0:
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
        planet()


# Main
start_menu()


