import random
# Assure-toi que ces imports fonctionnent selon ta structure de projet
from utils.input_utils import load_file, ask_text
from universe.character import add_item, display_character
from universe.house import update_house_points, display_winning_house
from chapter_1 import *
from chapter_2 import *


def learn_spells(character, file_path="../data/spells.json"):
    """
    Permet au personnage d'apprendre 5 sorts (1 Offensif, 1 Défensif, 3 Utilitaires).
    [cite: 657-662]
    """
    print("\nYou begin your magic lessons at Hogwarts...")  # [cite: 669]

    # 1. Chargement des sorts depuis le JSON
    all_spells = load_file(file_path)

    # 2. Séparation des sorts par catégorie pour respecter les quotas
    offensive_spells = []
    defensive_spells = []
    utility_spells = []

    # On trie les sorts disponibles dans le fichier
    for spell in all_spells:
        if spell['type'] == 'Offensive':
            offensive_spells.append(spell)
        elif spell['type'] == 'Defensive':
            defensive_spells.append(spell)
        elif spell['type'] == 'Utility':
            utility_spells.append(spell)

    learned_spells_list = []

    # 3. Sélection aléatoire des 5 sorts (1 Off, 1 Def, 3 Util)
    # On utilise une liste temporaire pour stocker les choix
    spells_to_learn = []

    # Choix du sort offensif (1)
    spells_to_learn.append(random.choice(offensive_spells))

    # Choix du sort défensif (1)
    spells_to_learn.append(random.choice(defensive_spells))

    # Choix des sorts utilitaires (3) - On boucle pour en prendre 3 uniques si possible
    # Note : Si la liste utilitaire est petite, random.choice peut prendre des doublons.
    # Ici on fait simple comme autorisé : 3 tirages.
    for i in range(3):
        spells_to_learn.append(random.choice(utility_spells))

    # 4. Apprentissage et affichage
    for spell in spells_to_learn:
        # Ajout au personnage via la fonction universe (clé 'Spells')
        # On suppose que add_item ajoute le nom ou l'objet complet.
        # Le sujet dit "The spell is added to the player's Spells list" [cite: 665]
        # et l'affichage final demande le nom et la description.
        # On va ajouter le dictionnaire complet ou juste le nom selon ton implémentation de add_item.
        # Ici, j'ajoute le dictionnaire pour pouvoir afficher la description à la fin.
        # Si ton add_item n'accepte que des strings, change ceci par spell['name'].

        # Pour rester cohérent avec display_character qui affiche souvent des strings,
        # on ajoute le Nom dans la liste 'Spells' du personnage,
        # mais on garde les détails dans learned_spells_list pour le résumé de ce chapitre.
        add_item(character, 'Spells', spell['name'])
        learned_spells_list.append(spell)

        print(f"You have just learned the spell: {spell['name']} ({spell['type']})")  # [cite: 670]
        input("Press Enter to continue...")

    # 5. Résumé final [cite: 676-679]
    print("\nYou have completed your basic spell training at Hogwarts!")
    print("Here are the spells you now master:")
    for spell in learned_spells_list:
        print(f"- {spell['name']} ({spell['type']}): {spell['description']}")


def magic_quiz(character, file_path="../data/magic_quiz.json"):
    """
    Lance un quiz interactif de 4 questions aléatoires.
    Retourne le nombre total de points gagnés.
    [cite: 680-684]
    """
    print("\nWelcome to the Hogwarts magic quiz!")  # [cite: 688]
    print("Answer the 4 questions correctly to earn points for your house.")

    # Chargement des questions
    all_questions = load_file(file_path)

    score = 0
    questions_asked = []

    # Boucle pour poser 4 questions
    while len(questions_asked) < 4:
        # Sélection aléatoire d'une question
        question = random.choice(all_questions)

        # Vérification pour ne pas poser deux fois la même question
        if question in questions_asked:
            continue

        questions_asked.append(question)
        question_number = len(questions_asked)

        # Affichage de la question
        print(f"\n{question_number}. {question['question']}")

        # Saisie de la réponse (utilisation de ask_text pour sécuriser l'input)
        # Le sujet ne précise pas ask_text ici mais c'est mieux. Sinon un simple input() suffit.
        user_answer = ask_text("> ")

        # Vérification de la réponse (insensible à la casse et aux espaces) [cite: 81, 90]
        # On compare la réponse utilisateur nettoyée avec la bonne réponse nettoyée
        if user_answer.strip().lower() == question['answer'].strip().lower():
            print("Correct answer! +25 points for your house.")  # [cite: 696]
            score += 25
        else:
            print(f"Wrong answer. The correct answer was: {question['answer']}")  # [cite: 693]

    print(f"\nScore obtained: {score} points")  # [cite: 704]
    return score


def start_chapter_3(character, houses):
    """
    Orchestre le déroulement du chapitre 3.
    [cite: 705-711]
    """
    # 1. Apprentissage des sorts
    learn_spells(character)

    # 2. Quiz de magie
    # On récupère les points gagnés
    points_earned = magic_quiz(character)

    # 3. Mise à jour des points de la maison du joueur
    # On suppose que le dictionnaire character a une clé 'House' définie au chapitre 2
    house_name = character.get('House', 'Gryffindor')  # Valeur par défaut si bug

    if points_earned > 0:
        update_house_points(houses, house_name, points_earned)

    # 4. Affichage de la maison en tête
    display_winning_house(houses)

    # 5. Affichage des informations complètes du joueur
    display_character(character)

    print("\nEnd of Chapter 3! You are now ready for greater challenges...")


start_chapter_3(character, houses)