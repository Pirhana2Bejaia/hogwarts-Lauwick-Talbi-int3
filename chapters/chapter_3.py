import random
from utils.input_utils import load_file, ask_text
from universe.character import add_item, display_character
from universe.house import update_house_points, display_winning_house


def learn_spells(character, file_path="data/spells.json"):
    print("=" * 40)
    print(" CHAPTER 3: MAGIC CLASSES ")
    print("=" * 40)

    print(""" 
You enter the Charms classroom. Small piles of books are stacked on the desks.
Professor Flitwick is standing on a pile of books to see the class.

'Welcome, young wizards! Today, we will learn new spells.'
'Remember: Swish and flick!'
    """)
    input("[Press Enter to start the lesson]")


    all_spells = load_file(file_path)


    offensive_spells = [s for s in all_spells if s['type'] == 'Offensive']
    defensive_spells = [s for s in all_spells if s['type'] == 'Defensive']
    utility_spells = [s for s in all_spells if s['type'] == 'Utility']

    spells_to_learn = []
    if offensive_spells:
        spells_to_learn.append(random.choice(offensive_spells))
    if defensive_spells:
        spells_to_learn.append(random.choice(defensive_spells))

    nb_utilitaires = 0

    max_util = 3

    while nb_utilitaires < max_util:
        sort = random.choice(utility_spells)
        if sort not in spells_to_learn:
            spells_to_learn.append(sort)
            nb_utilitaires = nb_utilitaires + 1

    learned_spells_list = []

    for spell in spells_to_learn:
        print("Professor Flitwick demonstrates the spell: " + spell['name'])
        print("Description: " + spell['description'])

        success = False
        while not success:
            user_try = ask_text("Type the incantation to cast it: ")

            if user_try.lower().strip() == spell['name'].lower().strip():
                print("✨ You wave your wand perfectly! " + spell['name'] + "!")
                success = True
            else:
                print("☁️ Nothing happens. Flitwick says: 'Watch your pronunciation! Try again.'")

        add_item(character, 'Spells', spell['name'])
        learned_spells_list.append(spell)

    print("\n'Excellent work!' squeaks Professor Flitwick.")
    print("You have mastered 5 new spells.")


def magic_quiz(character, file_path="data/magic_quiz.json"):

    print( "=" * 30)
    print(" THEORETICAL EXAM ")
    print("=" * 30)

    print("""
Later that day, you have a written exam on Magical Theory.
You sit down in the Great Hall. Hermione is whispering answers to herself nearby.
You decide to quickly read your notes one last time before the test begins.
    """)
    input("[Press Enter to revise your notes]")


    all_questions = load_file(file_path)



    print("--- YOUR STUDY NOTES ---")
    for q in all_questions:
        print("* Remember: " + q['answer'] + " is the answer to '" + q['question'] + "'")
    print("------------------------\n")

    print("Professor McGonagall takes away your notes.")
    print("'The exam begins now. No cheating!'")
    input("[Press Enter to start the Quiz]")

    score = 0
    questions_asked = []
    max_questions = 4

    while len(questions_asked) < max_questions:
        question = random.choice(all_questions)

        if question in questions_asked:
            continue

        questions_asked.append(question)
        print("Question " + str(len(questions_asked)) + ":")
        print(question['question'])

        user_answer = ask_text("> ")

        if user_answer.strip().lower() == question['answer'].strip().lower():
            print("Correct! (+25 points)")
            score = score + 25
        else:
            print("Wrong. The correct answer was: " + question['answer'])

    print("\nExam finished. You scored: " + str(score) + " points.")
    return score


def start_chapter_3(character, houses):

    learn_spells(character)

    points_earned = magic_quiz(character)

    house_name = character.get("House", "Gryffindor")

    if points_earned > 0:
        update_house_points(houses, house_name, points_earned)

    display_winning_house(houses)

    from universe.character import display_character
    display_character(character)

    print("End of Chapter 3! You are now ready for the Quidditch match...")
    input("[Press Enter to continue]")

    return character