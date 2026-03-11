# Libraries
import random
import time

# Global variables
own_characters = []
#enemy_characters = [{"Name" : }]
TEXT_SLEEP_TIME = 0.1

#Functions
def slow_type(sentence):
    for i in range(len(sentence)):
        print(sentence[i], end = "")
        time.sleep(TEXT_SLEEP_TIME)
    print()

def main_menu(): #Menu to run at start
    slow_type("You are stuck in space")
    time.sleep(0.5)
    slow_type("You will have to make your way back to Earth while completing challenges along the way.")
    time.sleep(0.5)


def name_check():
    global name
    name = input("What is your name? ")
    print(f"Your name is {name}")




#Main
main_menu()
#name_check()