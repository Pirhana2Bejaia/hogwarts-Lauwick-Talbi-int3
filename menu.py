from utils.input_utils import ask_choice
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2

def display_main_menu():
    print(" ⚡ HOGWARTS ADVENTURE ⚡ ")

def launch_menu_choice():
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0
    }
    while True:
        display_main_menu()
        choice = ask_choice("Main Menu", ["Start Adventure", "Exit the game"])
        if choice == 1:
            character = start_chapter_1()
            character = start_chapter_2(character)
        elif choice == 2:
            print("Goodbye, young wizard!")
            break
        else:
            print("Invalid choice.")