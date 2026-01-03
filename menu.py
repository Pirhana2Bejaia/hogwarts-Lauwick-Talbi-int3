from utils.input_utils import ask_choice
from chapters.chapter_1 import start_chapter_1
from chapters.chapter_2 import start_chapter_2
from chapters.chapter_3 import start_chapter_3
from chapters.chapter_4 import start_chapter_4_quidditch

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
        choice = ask_choice("An opportunity for adventure lies before you. Seize it and live the adventure, or stay where you are and live the same life every day.", ["Start Adventure", "Exit the game"])
        if choice == 1:
            character = start_chapter_1()
            character = start_chapter_2(character)
            character = start_chapter_3(character,houses)
            character = start_chapter_4_quidditch(character, houses)
            break
        elif choice == 2:
            print("Goodbye, young wizard!")
            break
        else:
            print("Invalid choice.")