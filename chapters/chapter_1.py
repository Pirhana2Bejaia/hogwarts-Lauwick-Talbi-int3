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

#introduction()

def create_character():
    last_name = ask_text("Enter your character's last name:")
    first_name = ask_text("Enter your character's first name:")

    # on pourrait faire une boucle pour obliger l'utilisateur à metter un prénom / nom correct
    # cad commençant par une majuscule t composé de lettre ou de '-'

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

player_tab = create_character()

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
    ~ Dear """+ last_name+' '+ first_name+ """,                     
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

        return exit()

    return ''

#receive_letter()

def meet_hagrid():
    first_name = player_tab["First Name"]
    hagrid = '''
            The minute you agreed, a flash of lightning dazzles you, and  a bearded        
            giant appeared in front of you.

    Hagrid: Hello ''' +first_name+ ''' sorcere! My name is Hagrid
            I’m here to help you with your back to school at Hogwarts
            shopping on DiagonAlley.

            '''
    print(hagrid)
    print()
    choice = ask_choice("Do you want to follow Hagrid ? ",["Yes, the beginning of a wonderful adventure",
                                                                            "you are petrified with fear 😵"])
    if choice == 1:
        print('follow me little man ! ')
    else:
        print('hagrid take your arms :Come on, young man, cheer up a little!')

    print()
    input("[ Press ENTER to continue]")
    print()


#meet_hagrid()

def buy_supplies():
    file = load_file("../data/inventory.json")
    money = player_tab["Money"]
    store = []
    for i in file:
        store.append(file[i])

    print('you have', money, ' $')
    print()
    input("[ Press ENTER to continue]")
    print()

    tentative = 3

    twins = []


    while tentative > 0:

        a = ask_choice('you must buy the three essential items: Magic wand, Wizard robe, and Potions book.',store)

        if a == 8 or a == 3 or a == 5 or a == 6 or a == 7 or a in twins:
            prohibited = """
            Haggrid :
                You should'nt buy this item you will not have enough money to buy the three essential items
            """
            print(prohibited)

        else:
            player_tab["Inventory"].append(store[a][0])
            tentative -= 1
            twins.append(a)

    return print(player_tab["Inventory"])




buy_supplies()

"""
This function allows to buy the required school supplies on Diagon Alley. The complete catalog is
loaded from the data/inventory.json file. The player must buy the three essential items: Magic
wand, Wizard robe, and Potions book.
Once these purchases have been made, the player must choose a pet from among the authorized
species:
• Owl - 20 galleons
• Cat - 15 galleons
• Rat - 10 galleons
• Toad - 5 galleons
Please note: The budget is checked before each purchase. If the player does not have enough
money or forgets a mandatory item, they lose the game.
Finally, the function displays the character's final inventory.
"""