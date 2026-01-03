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

        exit()

    return ''



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







def buy_supplies(character):
    """
    Manages the purchase of supplies on Diagon Alley.
    The player must buy mandatory items and choose a pet.
    """
    # Dictionnaire fourni dans ta consigne (normalement chargé via load_file)

    #test = load_file("data/inventory")


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

    print("\nWelcome to Diagon Alley!")  # [cite: 443]

    # BOUCLE D'ACHAT DES FOURNITURES
    # On continue tant qu'il reste des objets obligatoires à acheter
    while len(mandatory_items) > 0:
        print("\nCatalog of available items:")  # [cite: 444]

        # Affichage du catalogue
        # On parcourt les clés "1", "2", etc.
        # Le sujet demande d'afficher "(required)" à côté des objets obligatoires [cite: 450, 453]
        for key in inventory_data:
            item_name = inventory_data[key][0]
            item_price = inventory_data[key][1]

            display_text = key + ". " + item_name + " " + str(item_price) + " Galleons"

            # Vérification si l'objet est dans la liste des obligatoires
            is_required = False
            for req in mandatory_items:
                if req == item_name:
                    is_required = True

            if is_required:
                display_text += " (required)"

            print(display_text)

        # Affichage de l'argent et des objets manquants [cite: 459, 460]
        current_money = character['Money']
        print("\nYou have " + str(current_money) + " Galleons.")
        print("Remaining required items: " + ", ".join(mandatory_items))

        # Demande de choix (Source 461)
        choice = str(ask_number("Enter the number of the item to buy: ", 1, 8))

        # Récupération des infos de l'objet choisi
        selected_item = inventory_data[choice]
        name = selected_item[0]
        price = selected_item[1]

        # Vérification du budget
        if current_money >= price:
            # Achat validé
            modify_money(character, -price)  # Débit du compte [cite: 273]
            add_item(character, 'Inventory', name)  # Ajout à l'inventaire [cite: 276]
            print("You bought: " + name + " (-" + str(price) + " Galleons).")  # [cite: 462]

            # Si c'était un objet obligatoire, on le retire de la liste des tâches
            # On ne peut pas utiliser .remove() directement sans vérifier s'il est dedans
            if name in mandatory_items:
                mandatory_items.remove(name)
        else:
            # GAME OVER si le joueur ne peut pas payer un objet (Source 439-440)
            print("You don't have enough money for " + name + "!")
            print("Without your school supplies, you are expelled from Hogwarts before even starting.")
            print("Game Over.")
            exit()  # Arrêt immédiat du programme [cite: 409]

    print("\nAll required items have been purchased!")  # [cite: 468]

    # CHOIX DE L'ANIMAL DE COMPAGNIE
    print("It's time to choose your Hogwarts pet!")  # [cite: 469]
    print("You have " + str(character['Money']) + " Galleons.")  # [cite: 470]

    # Liste des animaux et prix imposés par le sujet [cite: 435-438]
    pets = [
        ["Owl", 20],
        ["Cat", 15],
        ["Rat", 10],
        ["Toad", 5]
    ]

    print("Available pets:")  # [cite: 471]
    for i in range(len(pets)):
        print(str(i + 1) + ". " + pets[i][0] + " " + str(pets[i][1]) + " Galleons")

    # Boucle pour forcer un achat valide d'animal
    pet_bought = False
    while not pet_bought:
        pet_choice = ask_number("Which pet do you want? ", 1, 4)  # [cite: 478]

        # -1 car l'utilisateur entre 1-4 mais la liste commence à 0
        selected_pet = pets[pet_choice - 1]
        pet_name = selected_pet[0]
        pet_price = selected_pet[1]

        if character['Money'] >= pet_price:
            modify_money(character, -pet_price)
            add_item(character, 'Inventory', pet_name)
            print("You chose: " + pet_name + " (-" + str(pet_price) + " Galleons).")  # [cite: 484]
            pet_bought = True
        else:
            print("You don't have enough money for a " + pet_name + ". Choose another one.")
            # Note : Si le joueur n'a même plus 5 gallions pour le crapaud,
            # il est bloqué, ce qui correspond à un échec du jeu.
            if character['Money'] < 5:
                print("You can't afford any pet! Game Over.")
                exit()

    print("All required items have been successfully purchased! Here is your final inventory:")  # [cite: 485]

    # Affichage final du personnage via la fonction demandée [cite: 253, 441]
    # display_character(character)
    # (J'ai commenté l'appel car je ne sais pas si tu as déjà importé cette fonction, mais c'est requis)



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