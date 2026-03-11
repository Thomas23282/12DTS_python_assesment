# Libraries
import random
import time

# Global variables
own_characters = []
#enemy_characters = [{"Name" : }]

#Functions
def main_menu(): #Menu to run at start
    print("You are stuck in space")
    time.sleep(0.5)
    print("You will have to make your way back to Earth while completing challenges along the way.")
    time.sleep(0.5)

def name_check():
    global name
    name = input("What is your name? ")
    print(f"Your name is {name}")

#Main
#main_menu()
name_check()