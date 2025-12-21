import random
# On garde uniquement les imports utiles
from utils.input_utils import load_file, ask_text
from universe.character import add_item, display_character
from universe.house import update_house_points, display_winning_house


# Note sur le chemin : Si tu lances le jeu depuis main.py, le chemin est "data/spells.json".
# Si tu lances ce fichier seul pour tester, c'est "../data/spells.json".
# Par défaut, on met le chemin relatif à main.py.

def learn_spells(character, file_path="data/spells.json"):
    """
    Permet au personnage d'apprendre 5 sorts (1 Offensif, 1 Défensif, 3 Utilitaires).
    [cite: 657-662]
    """
    print("\nYou begin your magic lessons at Hogwarts...")  # [cite: 669]

    # 1. Chargement des sorts
    # Si le fichier n'est pas trouvé, assure-toi que le dossier data est bien à la racine
    try:
        all_spells = load_file(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found. Check your path.")
        return

    # 2. Séparation des sorts par catégorie
    offensive_spells = [s for s in all_spells if s['type'] == 'Offensive']
    defensive_spells = [s for s in all_spells if s['type'] == 'Defensive']
    utility_spells = [s for s in all_spells if s['type'] == 'Utility']

    # 3. Sélection aléatoire
    spells_to_learn = []

    # Choix 1 Offensif et 1 Défensif
    # On vérifie que les listes ne sont pas vides pour éviter un crash
    if offensive_spells:
        spells_to_learn.append(random.choice(offensive_spells))
    if defensive_spells:
        spells_to_learn.append(random.choice(defensive_spells))

    # Choix 3 Utilitaires
    # Astuce : random.choices (avec s) peut prendre des doublons,
    # mais pour apprendre 3 sorts différents, on peut vérifier la taille de la liste.
    if len(utility_spells) >= 3:
        # On essaie d'éviter les doublons si possible, sinon random.choice dans une boucle comme tu as fait
        for _ in range(3):
            spells_to_learn.append(random.choice(utility_spells))
    else:
        spells_to_learn.extend(utility_spells)  # On prend tout ce qu'il y a si moins de 3

    # 4. Apprentissage
    learned_spells_list = []

    for spell in spells_to_learn:
        # Ajout au personnage
        add_item(character, 'Spells', spell['name'])
        learned_spells_list.append(spell)

        print(f"You have just learned the spell: {spell['name']} ({spell['type']})")  # [cite: 670]
        input("[Press Enter to continue...]")

    # 5. Résumé
    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for spell in learned_spells_list:
        print(f"- {spell['name']} ({spell['type']}): {spell['description']}")


def magic_quiz(character, file_path="data/magic_quiz.json"):
    """
    Lance un quiz interactif de 4 questions.
    [cite: 680-684]
    """
    print("\nWelcome to the Hogwarts magic quiz!")  # [cite: 688]
    print("Answer the 4 questions correctly to earn points for your house.")

    try:
        all_questions = load_file(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return 0

    score = 0
    questions_asked = []

    # On pose 4 questions maximum (ou moins si le fichier est petit)
    max_questions = min(4, len(all_questions))

    while len(questions_asked) < max_questions:
        question = random.choice(all_questions)

        if question in questions_asked:
            continue

        questions_asked.append(question)
        print(f"\n{len(questions_asked)}. {question['question']}")

        user_answer = ask_text("> ")

        # Comparaison insensible à la casse [cite: 81]
        if user_answer.strip().lower() == question['answer'].strip().lower():
            print("Correct answer! +25 points for your house.")
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {question['answer']}")

    print(f"\nScore obtained: {score} points")
    return score


def start_chapter_3(character, houses):
    """
    Orchestre le Chapitre 3.
    [cite: 705]
    """
    # 1. Apprentissage des sorts
    learn_spells(character)

    # 2. Quiz
    points_earned = magic_quiz(character)

    # 3. Mise à jour des points
    # On sécurise au cas où "House" n'est pas défini (test)
    house_name = character.get("House", "Gryffindor")

    if points_earned > 0:
        update_house_points(houses, house_name, points_earned)

    # 4. Affichage maison gagnante
    display_winning_house(houses)

    # 5. Affichage perso
    display_character(character)

    print("\nEnd of Chapter 3! You are now ready for greater challenges...")
    input("[Press Enter to continue]")

    return character  # Bonne pratique de retourner le perso


# PROTECTION INDISPENSABLE
if __name__ == "__main__":
    # Ce bloc sert UNIQUEMENT si tu testes ce fichier tout seul
    # Il ne s'exécutera pas quand le fichier sera importé par menu.py

    # Données fictives pour le test
    mock_character = {"Last Name": "Potter", "First Name": "Harry", "Money": 100, "Spells": [], "Inventory": [],
                      "Attributes": {}, "House": "Gryffindor"}
    mock_houses = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    # Attention aux chemins pour le test local : il faudra peut-être "../data/..." ici
    start_chapter_3(mock_character, mock_houses)