# Adventure_Game_The_Warlock's_Curse.py
# Written by Katherine Piette & Nathan Reckley

# Some assistance and guidance was provided by Scott Piette in regards
# to the development of the data retrieval process.

import csv

def intro():
    print("-----------------------------------------------------------")
    print("WELCOME to THE WARLOCK'S CURSE!!!!")
    print("-----------------------------------------------------------")
    print("This is a text based adventure game! Full of fun,")
    print("adventure, and magic... three very important things.")
    print("You will be playing as Sam, a lively youth with a taste ")
    print("for adventure. It is your job to get Sam out of this adventure")
    print("safely. To make sure this program runs correctly, please make")
    print("sure the program and the file KatieAdventureList.csv are saved on")
    print("your computer's desktop.")
    print()
    command = input("Would you like the game's instructions? (y/n) ")

    if command[0] == 'y' or command[0] == 'Y':
        instructions()
        
def instructions():
    print()
    print("In this magical world you move between rooms. In each room you can")
    print("'look' and 'go' but you need to specify the direction you want to 'look'")
    print("or 'go'. Valid directions are 'north', 'south', 'east', 'west'. For")
    print("example 'look north' will tell you what you see looking north and 'go")
    print("north' will take you there.")
    print("Alright, let the adventure begin!")




def prompt():
    x = input("What do you want to do? ")
    x.lower()

    return x

def search(name, rooms):
    return[element for element in rooms if element['room_name'] == name]

def navigate(next_room):
    print()
    print(next_room['description'])
    print()

    while True:
        x = prompt()
        x.lower()
        j = x.split()
        print()
    
        if j[0] == 'look':
            if j[1] == 'north':
                print(next_room['look_north'])
                print()
            elif j[1] == 'south':
                print(next_room['look_south'])
                print()
            elif j[1] == 'west':
                print(next_room['look_west'])
                print()
            elif j[1] == 'east':
                print(next_room['look_east'])
                print()
            else:
                print("Please type a real direction.")
                goto_room = 'bad'
            
        elif j[0] == 'go':
            if j[1] == 'north':
                goto_room = next_room['go_north']
            elif j[1] == 'south':
                goto_room = next_room['go_south']
            elif j[1] == 'west':
                goto_room = next_room['go_west']
            elif j[1] == 'east':
                goto_room = next_room['go_east']
            else:
                goto_room = 'bad'

            if goto_room == 'bad':
                print("Please type a real direction")
                print()
            else:
                if goto_room != 'None':
                    return goto_room
                else:
                    print("You can't go that way")

        else:
            print("I don't understand your command, commands are look and go")


def main():
    room_list = []
    
    intro()

    # Imports KatieAdventureList.csv and saves it as a dictionary.
    room_list = [row for row in csv.DictReader
                 (open("../Desktop/KatieAdventureList.csv"))]

    next_room = 'start' # This is the first room the game starts in.

    while next_room != 'exit' and next_room != 'victory' : 
        room = search(next_room, room_list)
        next_room = navigate(room[0]) # Room 0 in the csv file is the 'start'room

    if next_room == 'exit':
        print("YOU HAVE LOST")
    if next_room == 'victory':
        print("YOU HAVE WON! CONGRADULATIONS")

main()
    
