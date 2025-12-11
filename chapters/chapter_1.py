from utils.input_utils import *
from universe.character import *

def introduction():
    welcome_screen = """

                * .  |    .           .
          .   .      |       * .       .
             .      /^\           .    
        .  .       /   \      .        .     .
                  / | | \   * .
           |     /  |_|  \     | .
          /^\   |   _|_   |   /^\     .
          | |   |  |___|  |   | |         *
          |_|___|__|___|__|___|_|    .
          |  __   __    __   __ |
          | /  \ /  \  /  \ /  \|
          | |  | |  |  |  | |  ||  
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

          WELCOME TO THE WIZARDING WORLD
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

      Greetings, young wizard. 

      The stars have aligned and the owls have 
      been sent. You have been chosen to enter 
      Hogwarts School of Witchcraft and Wizardry.

      Your destiny awaits within these walls.

    [ Press ENTER to break the seal and begin ]
    """

    input(welcome_screen)

introduction()

def create_character():
    last_name = ask_text("Enter your character's last name:")
    first_name = ask_text("Enter your character's first name:")

    print("Choose your attributes:")

    atributes = {}

    atributes["Courage"] = ask_number("Choose your courage level (1-10): ", 1, 10)
    atributes["Intelligence"] = ask_number("Choose your courage level (1-10): ", 1, 10)
    atributes["Loyalty"] = ask_number("Choose your loyalty level (1-10): ", 1, 10)
    atributes["Ambition"] = ask_number("Choose your loyalty level (1-10): ", 1, 10)

    character = init_character(last_name, first_name, atributes)


    return display_character(character)

create_character()