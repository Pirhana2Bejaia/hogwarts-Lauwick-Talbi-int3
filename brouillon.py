def buy_supplies():
    file = load_file("../data/inventory.json")
    money = player_tab["Money"]
    store = []
    for i in file:
        store.append(file[i])

    print('you have', money, ' $')
    print()
    input("[ Press ENTER to continue]")
    print()

    tentative = 3

    twins = []


    while tentative > 0:

        a = ask_choice('you must buy the three essential items: Magic wand, Wizard robe, and Potions book.',store)

        if a == 8 or a == 3 or a == 5 or a == 6 or a == 7 or a in twins:
            prohibited = """
            Haggrid :
                You should'nt buy this item you will not have enough money to buy the three essential items
            """
            print(prohibited)

        else:
            player_tab["Inventory"].append(store[a][0])
            tentative -= 1
            twins.append(a)

    return print(player_tab["Inventory"])




buy_supplies()



import random
from utils.input_utils import load_file
from universe.house import update_house_points
def create_team(house_name, team_data, is_player=False, player=None):
    team = {
        'name': house_name,
        'score': 0,
        'goals_scored': 0,
        'goals_blocked': 0,
        'caught_snitch': False,
        'players': []
    }
    original_players = team_data["players"]
    if is_player and player :
        player_name = player['First Name'] + " " + player['Last Name'] + " (Seeker)"
        team['players'].append(player_name)
        for p in original_players[1:]:
            team['players'].append(p)
    else :
        team['players'] = original_players.copy()
    return team


def attempt_goal(attacking_team, defending_team, player_is_seeker=False):
    chance = random.randint(1, 10)
    if chance >= 6:
        attacking_team['score'] = attacking_team['score'] + 10
        attacking_team['goals_scored'] = attacking_team['goals_scored'] + 1
        if player_is_seeker:
            scorer = attacking_team['players'][0]
        else:
            scorer = random.choice(attacking_team['players'])
        print(" ⚽ GOAL! " + scorer + " scores for " + attacking_team['name'] + "! (+10 points)")
    else:
        defending_team['goals_blocked'] = defending_team['goals_blocked'] + 1
        print(" 🛡️ Missed! " + defending_team['name'] + " blocks the attack!")


def golden_snitch_appears():
    chance = random.randint(1, 6)
    if chance == 6:
        return True
    else:
        return False


def catch_golden_snitch(team1, team2):
    teams = [team1, team2]
    winner = random.choice(teams)
    winner['score'] = winner['score'] + 150
    winner['caught_snitch'] = True
    return winner

def display_score(team1, team2):
    print( "-"*20)
    print("Current Score:")
    print(team1['name'] + ": " + str(team1['score']))
    print(team2['name'] + ": " + str(team2['score']))
    print("-"*20 )

def display_team(team):
    print("Team " + team['name'] + ":")
    for player in team['players']:
        print("- " + player)


def quidditch_match(character, houses):
    print("=" * 40)
    print(" 🧹 THE QUIDDITCH MATCH BEGINS! 🧹 ")
    print("=" * 40)
    try:
        teams_data = load_file("data/teams_quidditch.json")
    except FileNotFoundError:
        print("Error: data/teams_quidditch.json not found.")
        return

    player_house = character.get("House", "Gryffindor")
    available_opponents = []
    for h in houses.keys():
        if h != player_house:
            available_opponents.append(h)

    opponent_house = random.choice(available_opponents)

    print( player_house + " VS " + opponent_house + "!")
    my_team = create_team(player_house, teams_data[player_house], is_player=True, player=character)
    opponent_team = create_team(opponent_house, teams_data[opponent_house])

    display_team(my_team)
    display_team(opponent_team)

    print("You are playing as the Seeker for " + player_house + "!")
    input("[Press Enter to start the match]")

    match_over = False
    turn = 1

    while turn <= 20 and match_over == False:
        print("--- Turn " + str(turn) + "/20 ---")
        input("[Press Enter for next turn]")

        attempt_goal(my_team, opponent_team, player_is_seeker=True)
        attempt_goal(opponent_team, my_team, player_is_seeker=False)
        display_score(my_team, opponent_team)
        if golden_snitch_appears():
            print("✨ THE GOLDEN SNITCH HAS BEEN SPOTTED! ✨")
            input("[Press Enter to see if someone catch it ]")
            snitch_winner = catch_golden_snitch(my_team, opponent_team)
            print("!!! " + snitch_winner['name'] + " CATCHES THE GOLDEN SNITCH (+150 POINTS) !!!")
            match_over = True
        turn = turn + 1

        if match_over == False:
            pass

    print( "=" * 40)
    print("FINAL SCORE")
    print(my_team['name'] + ": " + str(my_team['score']))
    print(opponent_team['name'] + ": " + str(opponent_team['score']))
    print("=" * 40)
    winner_house = ""
    if my_team['score'] > opponent_team['score']:
        print("🏆 VICTORY FOR " + player_house.upper() + "! 🏆")
        winner_house = player_house
    elif opponent_team['score'] > my_team['score']:
        print("Victory for " + opponent_house + "...")
        winner_house = opponent_house
    else:
        print("It's a DRAW! ")
    if winner_house != "":
        print( winner_house + " receives 500 points for the House Cup!")
        update_house_points(houses, winner_house, 500)

def start_chapter_4_quidditch(character, houses):
    quidditch_match(character, houses)

    print("End of Chapter 4! What an incredible performance on the field!")
    from universe.character import display_character
    print("FINAL CHARACTER STATUS ")
    display_character(character)
    print("=" * 40)
    print(" END OF THE SCHOOL YEAR ")
    print("=" * 40)

    print("""
    The Quidditch season is over, and exams are finished.
    All students gather in the Great Hall for the leaving feast.
    The Hall is decorated in the colors of the winning house.
        """)

    input("[Press Enter to listen to Dumbledore]")

    print("""
    Albus Dumbledore stands up at the High Table:
    'Another year gone!'
    'What a year it has been. Hopefully your heads are a little fuller than they were...'
    'And finally, let us celebrate our Quidditch champions!'

    The room erupts in cheers and throwing of hats.
    You enjoy a delicious meal of roast chicken, pies, and pumpkin juice.

    Tomorrow, the Hogwarts Express will take you back home.
    But you know that Hogwarts will always be there to welcome you back.

    Thank you for playing Hogwarts Adventure!
        """)
    return character