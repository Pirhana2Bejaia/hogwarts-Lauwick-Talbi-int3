'''
la première condition vérifie que l'input n'est pas vide
si elle n'est pas vide:
on vérifie que le message ne contient pas que des espaces blancs
'''


def ask_text(message):
    ask = input(message)

    checker = "not check"

    if len(ask) == 0:
        return ask_text(message)

    else:

        for i in range(len(ask)):
            if ask[i] != " ":
                checker = "check"

        if checker != "check":
            return ask_text(message)
        else:
            return '✅'