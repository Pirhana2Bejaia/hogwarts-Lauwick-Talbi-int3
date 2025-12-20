'''
la première condition vérifie que l'input n'est pas vide
si elle n'est pas vide:
on vérifie que le message ne contient pas que des espaces blancs
'''

def load_file(file_path):
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

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
            return ask

def ask_choice(message,options):
    print()
    for i in range(len(options)):
        print(i+1,'. ',options[i])
        print()
    answer = ask_number(message,1,len(options))
    return answer



def ask_number(message, min_val=None, max_val=None):
    negative = 'false'
    check = 'ok'
    answer = input(message)

    if len(answer) == 0:
        check = 'error'

    if len(answer) != 0:
        if answer[0] == '-':
            negative = 'true'
            answer = answer[1:]

    else:
        negative = 'false'

    for i in range(len(answer)):
        if ord(answer[i]) > 57 or ord(answer[i]) < 48:
            check = 'error'

    if check == 'ok':
        if negative == 'true':
            answer = -int(answer)
        else:
            answer = int(answer)

    if check == 'ok':
        if min_val != None:
            if min_val > answer or answer > max_val:
                check = 'error'

    while check == 'error':
        print("Please enter a number between", min_val, "and", max_val, ".")
        answer = input(message)
        check = 'ok'

        if len(answer) == 0:
            check = 'error'

        if len(answer) != 0:
            if answer[0] == '-':
                negative = 'true'
                answer = answer[1:]
            else:
                negative = 'false'

        for i in range(len(answer)):
            if ord(answer[i]) > 57 or ord(answer[i]) < 48:
                check = 'error'

        if check == 'ok':
            if negative == 'true':
                answer = -int(answer)
            else:
                answer = int(answer)

        if check == 'ok':
            if min_val != None and max_val != None:
                if min_val > answer or answer > max_val:
                    check = 'error'

    return answer


