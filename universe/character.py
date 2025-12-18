def init_character(last_name, first_name, attributes):
    dico = {"Last Name": last_name,
            "First Name": first_name,
            "Money": 100,
            "Inventory": [],
            "Spells": [],
            "Attributes": attributes}
    return dico


def display_character(character):
    print()
    print("Character profile:")
    print()
    for i in character:
        temporary = i

        if isinstance(character[i], dict): #Vérifie le type de la valeur, si c'est un dictionnaire alors on

            for j in character[i]:         # on affiche chaque element du dictionnaire
                print('-',j,' : ',character[i][j])

        elif isinstance(character[i], list):

            if len(character[i]) == 0 :
                print("You have no",temporary)

            for k in character[i]:
                print('-',k)

        else:
            print(i,':', character[i])
        print()
    return ''
# dans la ligne au dessus je renvoie une chaine de caractere vide pour evider de renvoyer NON

def modify_money(character, amount):
    character["Money"] += amount
    return character["Money"]


def add_item(character, key, item):
    character[key].append(item)
    return character[key]
