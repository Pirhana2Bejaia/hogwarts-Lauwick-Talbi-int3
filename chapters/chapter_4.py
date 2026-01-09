import random
from utils.input_utils import load_file
from universe.house import update_house_points, display_winning_house
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


def play_one_match(character, opponent_house, teams_data):

    player_house = character["House"]

    print( "=" * 30)
    print(" MATCH: " + player_house.upper() + " VS " + opponent_house.upper())
    print("=" * 30)
    my_team = create_team(player_house, teams_data[player_house], is_player=True, player=character)
    opponent_team = create_team(opponent_house, teams_data[opponent_house])

    print("You are facing " + opponent_house + "!")
    print("Captain " + teams_data[opponent_house]["captain"] + " shakes your hand.")
    input("[Press Enter to start kickoff]")

    match_over = False
    turn = 1
    max_turns = 10

    while turn <= max_turns and match_over == False:
        print("--- Turn " + str(turn) + "/" + str(max_turns) + " ---")

        attempt_goal(my_team, opponent_team, player_is_seeker=True)
        attempt_goal(opponent_team, my_team, player_is_seeker=False)
        display_score(my_team, opponent_team)

        if golden_snitch_appears():
            print("✨ THE GOLDEN SNITCH HAS BEEN SPOTTED! ✨")
            input("[Press Enter to dive!]")
            snitch_winner = catch_golden_snitch(my_team, opponent_team)
            print("!!! " + snitch_winner['name'] + " CATCHES THE GOLDEN SNITCH (+150 POINTS) !!!")
            match_over = True

        turn = turn + 1

    print("FINAL SCORE: " + my_team['name'] + " " + str(my_team['score']) + " - " + str(opponent_team['score']) + " " +
          opponent_team['name'])

    if my_team['score'] > opponent_team['score']:
        print("🏆 YOU WON THE MATCH!")
        return "Victory"
    elif opponent_team['score'] > my_team['score']:
        print("❌ YOU LOST THE MATCH...")
        return "Defeat"
    else:
        print("🤝 IT'S A DRAW.")
        return "Draw"


def simulate_ai_match(house1, house2):

    print("Simulating match: " + house1 + " vs " + house2 + "...")

    score1 = random.randint(0, 15) * 10
    score2 = random.randint(0, 15) * 10

    if random.choice([True, False]):
        score1 = score1 + 150
    else:
        score2 = score2 + 150

    print("Result: " + house1 + " (" + str(score1) + ") - " + house2 + " (" + str(score2) + ")")

    if score1 > score2:
        return house1
    elif score2 > score1:
        return house2
    else:
        return "Draw"


def start_chapter_4_quidditch(character, houses):
    print("=" * 40)
    print(" CHAPTER 4: THE QUIDDITCH CUP ")
    print("=" * 40)

    print("""
The Quidditch season is finally here!
This year is a full tournament.
Your house will play against all three other houses.
Wins grant 3 points. Draws grant 1 point.
    """)
    input("[Press Enter to see the schedule]")

    teams_data = load_file("data/teams_quidditch.json")


    player_house = character["House"]

    league_table = {
        "Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0
    }

    opponents = []
    for h in houses.keys():
        if h != player_house:
            opponents.append(h)

    result = play_one_match(character, opponents[0], teams_data)
    if result == "Victory":
        league_table[player_house] += 3
    elif result == "Draw":
        league_table[player_house] += 1
    else:
        league_table[opponents[0]] += 3

    winner_ai = simulate_ai_match(opponents[1], opponents[2])
    if winner_ai != "Draw": league_table[winner_ai] += 3

    input("[Press Enter for Match 2]")

    result = play_one_match(character, opponents[1], teams_data)
    if result == "Victory":
        league_table[player_house] += 3
    elif result == "Draw":
        league_table[player_house] += 1
    else:
        league_table[opponents[1]] += 3

    winner_ai = simulate_ai_match(opponents[0], opponents[2])
    if winner_ai != "Draw": league_table[winner_ai] += 3

    input("[Press Enter for the Final Match]")

    result = play_one_match(character, opponents[2], teams_data)
    if result == "Victory":
        league_table[player_house] += 3
    elif result == "Draw":
        league_table[player_house] += 1
    else:
        league_table[opponents[2]] += 3

    winner_ai = simulate_ai_match(opponents[0], opponents[1])
    if winner_ai != "Draw": league_table[winner_ai] += 3

    print( "=" * 30)
    print(" FINAL TOURNAMENT STANDINGS ")
    print("=" * 30)

    max_score = -1
    winner_house = ""

    for house in league_table:
        pts = league_table[house]
        print(house + ": " + str(pts) + " points")
        if pts > max_score:
            max_score = pts
            winner_house = house

    if winner_house == player_house:
        print("🏆 CONGRATULATIONS! Your house won the Cup!")
        update_house_points(houses, player_house, 500)
    else:
        print(winner_house + " won the Cup this year.")
        update_house_points(houses, winner_house, 500)
    print("\n" + "=" * 40)
    print(" THE END OF YEAR FEAST ")
    print("=" * 40)

    print("""
    The exams are finished. The trunks are packed.
    It is time for the Leaving Feast in the Great Hall.
    The Hall is decked out in the colors of the Quidditch winner.
        """)

    input("[Press Enter to sit at your table]")

    print("""
    Albus Dumbledore rises from the High Table. The chatter dies away.

    'Another year gone!' Dumbledore says cheerfully.
    'And now, as I understand it, the House Cup needs awarding...'
        """)

    input("[Press Enter to listen]")

    print("""
    'The points have been calculated...'
    'There has been some formidable magic this year...'
    'And some spectacular Quidditch matches...'
        """)

    print("Dumbledore pauses for effect. The Hall is silent.")
    print("...")
    input("[Press Enter for the result]")

    display_winning_house(houses)

    print("""
    'Congratulations to the winners!' shouts Dumbledore.
    Caps are thrown in the air. The feast appears on the golden plates.

    Tomorrow, the Hogwarts Express will take you back home.
    But Hogwarts will always be there to welcome you back.
        """)

    from universe.character import display_character
    print(" FINAL CHARACTER STATUS ")
    display_character(character)

    return character
