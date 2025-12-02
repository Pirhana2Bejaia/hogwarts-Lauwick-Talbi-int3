def ask_number(message,min_val,max_val):
    answer = int(input(message))
    if answer < min_val or answer > max_val:
        print("Please enter a number between", min_val, "and", max_val, ".")
        answer = int(input(message))
    return answer
def load_file(file_path):
    import json
    with open(file_path, 'r', encoding='utf-8') as f:
        '''le r correspond a read et le encoding='utf-8' fait que ça accepte les accent et caratère spéciaux '''
        data = json.load(f)
    return data
    ''' Exemple fictif d'utilisation dans chapter_1.py
from utils.input_utils import load_file

# On charge le fichier situé dans le dossier data
inventory_data = load_file("data/inventory.json")

# inventory_data sera maintenant une liste ou un dictionnaire exploitable
print(inventory_data)'''

