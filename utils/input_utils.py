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

def ask_choice(message,options):
    min = 1
    max = len(options)
    print(message)
    print()
    for i in range(len(options)):
        print(i+1,options[i])
    return ask_number(message,min,max)


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


print(ask_number('votre age : ', -15, 15))
def load_file(file_path):
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        '''le r correspond a read et le encoding='utf-8' fait que ça accepte les accent et caratère spéciaux '''
        data = json.load(f)
    '''# Exemple fictif d'utilisation dans chapter_1.py
from utils.input_utils import load_file

On charge le fichier situé dans le dossier data
inventory_data = load_file("data/inventory.json")

inventory_data sera maintenant une liste ou un dictionnaire exploitable
print(inventory_data)'''
    return data
