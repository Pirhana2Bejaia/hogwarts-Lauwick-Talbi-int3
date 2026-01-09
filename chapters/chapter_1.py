from utils.input_utils import *
from universe.character import *
from data import *

a = '‍🐦‍🔥🔥🪶🦇🕸️🕰️🦉🪽🧑‍🎓✨💎🗡️🏹🛡️⚔️💸💰🪙♨️⚡💫❌'


def introduction():
    welcome_screen = """

                ✨ . 🏳️    .           .
          .   .      |       ✨ .       .
             .      /^\           .    
        .  .       /   \      .        .     .
                  / | | \   ✨ .
           |     /  |_|  \     | .
          /^\   |   _¤_   |   /^\     .
          | |   |  |___|  |   | |        ✨
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


def create_character():
    last_name = ask_text("Enter your character's last name:")
    first_name = ask_text("Enter your character's first name:")


    print("Choose your attributes:")

    atributes = {}

    atributes["Courage"] = ask_number("Choose your courage level (1-10): ", 1, 10)
    atributes["Intelligence"] = ask_number("Choose your Intellingence level (1-10): ", 1, 10)
    atributes["Loyalty"] = ask_number("Choose your loyalty level (1-10): ", 1, 10)
    atributes["Ambition"] = ask_number("Choose your Ambition level (1-10): ", 1, 10)

    character = init_character(last_name, first_name, atributes)

    display_character(character)

    input("[ Press ENTER to continue]")

    return character


def receive_letter():
    last_name = player_tab["Last Name"]
    first_name = player_tab["First Name"]

    letter = """

    An owl flies through the window, delivering a 
    letter sealed with the Hogwarts crest...

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ~///////////////////////////////////////////////~                                                                                                 
    ~                                               ~
    ~               HOWARTS SCHOOL OF               ~
    ~            WITCHCRAFT AND WIZARDERY           ~     
    ~                                               ~
    ~ Dear """ + last_name + ' ' + first_name + """,                     
    ~                                               ~
    ~ We are pleased to inform you that you have a  ~
    ~ place at                                      ~
    ~ Hogwarts School of Witchcraft and Wizadry     ~
    ~ Please find enclosed alist of all necessary   ~
    ~ books and equipement.                         ~
    ~                                               ~
    ~ Term begins on 1 September. We await your owl ~
    ~ by no later than 31 july                      ~
    ~                                               ~
    ~                                               ~
    ~ Your sincerely,                               ~
    ~                                               ~
    ~ Minerva McGonagall                            ~
    ~ Deputy Headmistress                           ~
    ~                                               ~
    ~///////////////////////////////////////////////~ 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                [ Press ENTER to continue ]
    """

    input(letter)

    answer = ask_choice("Do you accept this invitation and go to Hogwarts ? ",
                        ["Yes, of course!", "No, I'd rather stay with Uncle Vernon..."])

    if answer == 1:
        print()
        print("a feeling of excitement rises within you")
        input('[ Press ENTER to continue ]')


    else:
        print("You tear up the letter, and Uncle Vernon cheers: EXCELLENT! Finally, someone NORMAL in this house!")
        print()
        print("The magical world will never know you existed... Game over.")

        exit()

    return ''


def meet_hagrid():
    first_name = player_tab["First Name"]
    hagrid = '''
            The minute you agreed, a flash of lightning dazzles you, and  a bearded        
            giant appeared in front of you.

    Hagrid: Hello ''' + first_name + ''' sorcere! My name is Hagrid
            I’m here to help you with your back to school at Hogwarts
            shopping on DiagonAlley.

            '''
    print(hagrid)
    print()
    choice = ask_choice("Do you want to follow Hagrid ? ", ["Yes, the beginning of a wonderful adventure",
                                                            "you are petrified with fear 😵"])
    if choice == 1:
        print('follow me little man ! ')
    else:
        print('hagrid take your arms :Come on, young man, cheer up a little!')

    print()
    input("[ Press ENTER to continue]")
    print()


def buy_supplies(character):

    inventory_data = {
        "1": ["Magic Wand", 35],
        "2": ["Wizard Robe", 20],
        "3": ["Tin Cauldron", 15],
        "4": ["Potions Book", 25],
        "5": ["Magic Quill", 5],
        "6": ["Enchanted Book", 30],
        "7": ["Copper Scale", 10],
        "8": ["Invisibility Cloak", 100]
    }

    mandatory_items = ["Magic Wand", "Wizard Robe", "Potions Book"]

    print("\nWelcome to Diagon Alley!")
    while len(mandatory_items) > 0:
        print("\nCatalog of available items:")


        for key in inventory_data:
            item_name = inventory_data[key][0]
            item_price = inventory_data[key][1]

            display_text = key + ". " + item_name + " " + str(item_price) + " Galleons"

            is_required = False
            for req in mandatory_items:
                if req == item_name:
                    is_required = True

            if is_required:
                display_text += " (required)"

            print(display_text)

        current_money = character['Money']
        print("\nYou have " + str(current_money) + " Galleons.")
        print("Remaining required items: " + ", ".join(mandatory_items))

        choice = str(ask_number("Enter the number of the item to buy: ", 1, 8))

        selected_item = inventory_data[choice]
        name = selected_item[0]
        price = selected_item[1]


        if current_money >= price:

            modify_money(character, -price)
            add_item(character, 'Inventory', name)
            print("You bought: " + name + " (-" + str(price) + " Galleons).")

            if name in mandatory_items:
                mandatory_items.remove(name)
        else:

            print("You don't have enough money for " + name + "!")
            print("Without your school supplies, you are expelled from Hogwarts before even starting.")
            print("Game Over.")
            exit()

    print("\nAll required items have been purchased!")


    print("It's time to choose your Hogwarts pet!")
    print("You have " + str(character['Money']) + " Galleons.")

    pets = [
        ["Owl", 20],
        ["Cat", 15],
        ["Rat", 10],
        ["Toad", 5]
    ]

    print("Available pets:")
    for i in range(len(pets)):
        print(str(i + 1) + ". " + pets[i][0] + " " + str(pets[i][1]) + " Galleons")

    pet_bought = False
    while not pet_bought:
        pet_choice = ask_number("Which pet do you want? ", 1, 4)
        selected_pet = pets[pet_choice - 1]
        pet_name = selected_pet[0]
        pet_price = selected_pet[1]

        if character['Money'] >= pet_price:
            modify_money(character, -pet_price)
            add_item(character, 'Inventory', pet_name)
            print("You chose: " + pet_name + " (-" + str(pet_price) + " Galleons).")
            pet_bought = True
        else:
            print("You don't have enough money for a " + pet_name + ". Choose another one.")

            if character['Money'] < 5:
                print("You can't afford any pet! Game Over.")
                exit()

    print("All required items have been successfully purchased! Here is your final inventory:")


def start_chapter_1():
    global player_tab

    introduction()
    player_tab = create_character()
    receive_letter()
    meet_hagrid()
    buy_supplies(player_tab)

    print("\n" + "~" * 40)
    print("End of Chapter 1! Your adventure begins at Hogwarts...")
    print("~" * 40)
    input("[ Press ENTER to continue to Chapter 2 ]")

    return player_tab