def init_character(last_name, first_name, attributes):
    dico = {"Last Name": last_name,
            "First Name": first_name,
            "Money": 100,
            "Inventory": [],
            "Spells": [],
            "Attributes": attributes}
    return dico


def display_character(character):
    print("Character profile:")
    for i in character:
        print(i, character[i])
    return ''
# dans la ligne au dessus je renvoie une chaine de caractere vide pour evider de renvoyer NONZ

def modify_money(character, amount):
    character["Money"] += amount
    return character["Money"]


def add_item(character, key, item):
    character[key].append(item)
    return character[key]
