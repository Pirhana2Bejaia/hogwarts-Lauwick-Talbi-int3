# hogwarts-Lauwick-Talbi-int3
Hogwart

## 1. General Presentation

Project Title: Hogwarts Adventure: The Art of Coding like a Wizard

Brief Description:
This project is an interactive text-based adventure game developed in Python as part of the TI101I course. It immerses the player in the world of Harry Potter, allowing them to embody a young wizard or witch taking their first steps at Hogwarts.

The game unfolds in four chapters. The first chapter covers the arrival, character creation, and shopping on Diagon Alley. The second chapter covers the journey, meeting iconic characters, and the Sorting Ceremony. The third chapter covers learning magic spells and a knowledge quiz. The fourth chapter covers the conclusion with the Quidditch Cup tournament.

This project implements key programming concepts such as dictionary and list manipulation, modular functions, user input management, and external JSON file handling.

Contributors:
Talbi Mael 
Adrien Lauwick 

## 2. Installation

Prerequisites:
You need Python 3.x installed on your machine. You also need a terminal or an IDE (like PyCharm or VS Code) that supports UTF-8 encoding.

Cloning the repository:
To retrieve the project source code, execute the following command in your terminal:

git clone 
cd hogwarts-adventure

Environment Configuration:
No external libraries are required. The project uses only standard Python libraries (random, json). Ensure the file structure is respected for data loading to work correctly:

hogwarts/
  main.py
  menu.py
  data/
    houses.json
    inventory.json
    magic_quiz.json
    spells.json
    teams_quidditch.json
  utils/
  universe/
  chapters/

## 3. Usage

Launching the Application:
The entry point of the game is the main.py file. To start the adventure, execute the following command from the project root:

python main.py

Navigation:
The game is played entirely using the keyboard. For menus, type the number corresponding to your choice (e.g., 1, 2) and press Enter. For text input, type your answer (name, spell incantation) and validate. To progress, press Enter when the game displays narrative pauses.

Example Usage:
HOGWARTS ADVENTURE
1. Start Adventure
2. Exit the game
Your choice: 1
Enter your character's last name: Potter
Enter your character's first name: Harry

## 4. Key Features

The application integrates the following main features:

Role-Playing Game (RPG) System: Management of character attributes (Courage, Intelligence, Loyalty, Ambition) that evolve based on dialogue choices. It also includes inventory and budget management using Galleons.

Sorting Algorithm: An assign_house function determines the player's house (Gryffindor, Slytherin, etc.) by combining their attributes and their answers to a personality test.

Game and Combat System (Quidditch): Simulation of a complete tournament with score management, goal probabilities, and Golden Snitch capture mechanics.

Data Management: Dynamic loading of quiz questions, spell lists, Quidditch teams, and house descriptions from external JSON files.

Input Validation: Robust utility functions found in input_utils.py ensure the game does not crash due to typing errors, checking for correct types and value ranges.

## 5. Logbook

Project Timeline:
Week 1: Setup of Git architecture. Development of utility modules (input_utils.py) and character creation (chapter_1.py, character.py).
Week 2: Implementation of house logic and the journey to Hogwarts (chapter_2.py, house.py). JSON file management.
Week 3: Development of magic classes and the quiz (chapter_3.py). Interim submission.
Week 4: Finalization of the Quidditch tournament (chapter_4.py). Global integration via menu.py and main.py. Final tests and README writing.

Task Distribution:
mael talbi Responsible for : input_utils.py, chapter_1, chapter_3, character.py
Adrien Lauwick: Responsible for chapter_3, chapter_4, house.py, common: Debugging, JSON file creation, and integration tests.

## 6. Control, Testing, and Validation

Input and Error Management:
The utils/input_utils.py module ensures game stability. The ask_number function checks that input is numeric, handles negative numbers if needed, and loops until the value is within the specified range. The ask_text function prevents empty strings or whitespace-only inputs. The load_file function uses error handling to manage missing JSON files.

Known Bugs:
On some Windows terminals (cmd.exe), emojis may not display correctly due to encoding issues. Using the new Windows Terminal or VS Code is recommended. Although case sensitivity is handled for spells, some specific inputs may require exact typing.

Testing Strategies:
Manual tests were performed at each stage. Unit tests verified that the player is correctly added as a Seeker in the team creation function. Limit tests checked scenarios like trying to buy items without money. Integration tests involved a complete playthrough from Chapter 1 to 4 to verify the continuity of character attributes and house scores.
"""