from chapters.chapter_1 import start_chapter_1
from utils.input_utils import ask_choice
from universe.house import assign_house
from utils.input_utils import load_file
from universe.character import display_character
questions = [("You see a friend in danger. What do you do?",
 ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
 ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),
 ("Which trait describes you best?",
 ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
 ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),
 ("When faced with a difficult challenge, you...",
 ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends","Analyze the problem"],
 ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])]
def meet_friends(character):
    ron = """
    "You board the Hogwarts Express. The train slowly departs northward..."
    "A red-haired boy enters your compartment, looking friendly."
    - Hi! I'm Ron Weasley. Mind if I sit with you? 
    """
    print(ron)
    a = ask_choice("How do you respond ?", [" Sure, have a seat!"," Sorry, I prefer to travel alone."])
    print("Your choice :",a)
    if a == 1:
        character["Attributes"]["Loyalty"] += 1
        print("Ron smiles: "
              "— Awesome! You'll see, Hogwarts is amazing!")
    if a == 2:
        character["Attributes"]["Ambition"] += 1
        print("Ron feel disappointed: "
              "- It's okay ...... "
              "See you next time!")
    hermione = """
    A girl enters next, already carrying a stack of books.
    - Hello, I'm Hermione Granger. Have you ever read 'A History of Magic'?
    """
    print(hermione)
    a = ask_choice("How do you respond ?",[" Yes, I love learning new things!"," Uh… no, I prefer adventures over books."])
    print("Your choice :", a)
    if a == 1:
        character["Attributes"]["Intelligence"] += 1
        print("Hermione smiles, impressed"
              ": — Oh, that's rare! You must be very clever!")
    if a == 2:
        character["Attributes"]["Courage"] += 1
        print("Hermione cried "
              "- Your not clever your not my friend")
    drago = """
    Then a blonde boy enters, looking arrogant.
    - I'm Draco Malfoy. It's best to choose your friends carefully from the start, don't you think?
    """
    print(drago)
    a=ask_choice("How do you respond?",[" Shake his hand politely.", " Ignore him completely.", " Respond with arrogance."])
    print("Your choice :", a)
    if a == 1:
        character["Attributes"]["Ambition"] += 1
        print("Drago smiles: "
              "- Happy to get you as a new friend")
    if a == 2:
        character["Attributes"]["Loyalty"] += 1
        print("Draco frowns, annoyed. "
              "— You'll regret that!")
    if a == 3:
        character["Attributes"]["Courage"] += 1
        print("Drago frowns, annoyed. "
              "- You think your intelligent POTTER")
    print("""
    The train continues its journey. Hogwarts Castle appears on the horizon...
    Your choices already say a lot about your personality!""")
    input("[Press ENTER to continue]")
    print(f"Your updated attributes: {character['Attributes']}")
def welcome_message():
    print( """
        You enter the Great Hall, looking up at the enchanted ceiling reflecting the starry sky.
        Professor Dumbledore rises from the head table, beaming at the students.

        "Welcome! Welcome to a new year at Hogwarts!

        Before we begin our banquet, I would like to say a few words.
        To our new students, welcome to your new home. To our old students, welcome back.

        Remember, help will always be given at Hogwarts to those who ask for it.
        But now, I know you are all hungry... Let the feast begin!"
        """)
    input("[Press Enter to join the feast and start the Ceremony]")
def sorting_ceremony(character):
    print("The sorting ceremony begins in the Great Hall...")
    print("The Sorting Hat observes you for a long time before asking its questions:")
    questions = [
        ("You see a friend in danger. What do you do?",
         ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
         ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),

        ("Which trait describes you best?",
         ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
         ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),

        ("When faced with a difficult challenge, you...",
         ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends", "Analyze the problem"],
         ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])
    ]
    assigned_house = assign_house(character, questions)
    character["House"] = assigned_house
    print(f"The Sorting Hat exclaims: {assigned_house.upper()}!!!")
    print(f"You join the {assigned_house} students to loud cheers!")
    return assigned_house
def enter_common_room(character):
    houses_data = load_file("data/houses.json")
    house_name = character["House"]
    if house_name in houses_data:
        house_info = houses_data[house_name]
    else:
        print(f"Error: House '{house_name}' not found in database.")
        return
    print("You follow the prefects through the castle corridors...")
    print(f"{house_info['description']}")
    print(f"{house_info['installation_message']}")
    colors_string = ", ".join(house_info['colors'])
    print(f"Your house colors: {colors_string}")
    input("[Press Enter to settle into your new dormitory]")


def start_chapter_2(character):
    print("=" * 40)
    print(" CHAPTER 2: THE HOGWARTS EXPRESS ")
    print("=" * 40)
    print("""
    You arrive at King's Cross Station in London.
    You push your trolley, looking for Platform 9 3/4.
    But you only see platforms 9 and 10...
        """)

    input("[Press Enter to look around]")

    print("""
    Suddenly, you hear a woman's voice:
    'Packed with Muggles, of course! Come on, Percy, you go first.'
    You see a family with flaming red hair.
        """)
    choice = ask_choice("What do you do?", ["Ask for help", "Watch them silently"])

    if choice == 1:
        print("""
    You approach the woman. She smiles kindly at you.
    'First time at Hogwarts? Ron is new too.'
    She points at a brick wall between platforms 9 and 10.
    'All you have to do is walk straight at the barrier.'
    'Don't stop and don't be scared you'll crash into it.'
            """)
    else:
        print("""
    You watch a boy run straight at the solid brick wall...
    And he vanishes right through it!
    You take a deep breath, close your eyes, and run.
            """)

    print("""
    ...
    You open your eyes. A scarlet steam engine is waiting for you.
    Welcome to Platform 9 3/4!
        """)

    input("[Press Enter to board the train]")
    meet_friends(character)
    welcome_message()
    sorting_ceremony(character)
    enter_common_room(character)
    print("📋 END OF CHAPTER 2 STATUS 📋")
    display_character(character)
    print("End of Chapter 2! Your adventure begins at Hogwarts...")
    print("Classes are about to start.")
    input("[Press Enter to continue]")
    return character

