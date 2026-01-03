from utils.input_utils import ask_choice
def update_house_points(houses, house_name, points):
    while house_name != "Gryffindor" and house_name != "Slytherin" and house_name != "Hufflepuff" and house_name != "Ravenclaw":
        house_name = input("Please enter the house's name: ")
    houses[house_name] = houses[house_name] + points
    return


def display_winning_house(houses):
    max_points = -1
    for house in houses:
        if houses[house] > max_points:
            max_points = houses[house]

    winners = []
    for house in houses:
        if houses[house] == max_points:
            winners.append(house)
    if len(winners) > 1:
        # Cas d'égalité
        print("We have a tie between: " + " and ".join(winners))
        print("They both have " + str(max_points) + " points.")
    else:
        print("The winner is " + winners[0] + " with " + str(max_points) + " points.")
def assign_house(character, questions):
    houses = {
        "Gryffindor": 0,
        "Slytherin": 0,
        "Hufflepuff": 0,
        "Ravenclaw": 0,
    }
    for key in character["Attributes"].keys():
        attr_name = key.capitalize()
        if attr_name == "Courage":
            update_house_points(houses, "Gryffindor", 2 * character["Attributes"][key])
        elif attr_name == "Ambition":
            update_house_points(houses, "Slytherin", 2 * character["Attributes"][key])
        elif attr_name == "Loyalty":
            update_house_points(houses, "Hufflepuff", 2 * character["Attributes"][key])
        elif attr_name == "Intelligence":
            update_house_points(houses, "Ravenclaw", 2 * character["Attributes"][key])
    for question in questions:
        print("\n" + question[0])
        a = ask_choice("Your answer: ", question[1])
        update_house_points(houses, question[2][a - 1], 3)
    max_point = -1
    name_house = ""
    for name in houses.keys():
        if houses[name] > max_point:
            max_point = houses[name]
            name_house = name

    return name_house