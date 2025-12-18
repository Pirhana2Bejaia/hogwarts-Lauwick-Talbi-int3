def update_house_points(houses, house_name, points):
    while house_name != "Gryffindor" and house_name != "Slytherin" and house_name != "Hufflepuff" and house_name != "Ravenclaw":
        house_name = input("Please enter the house's name: ")
    houses[house_name] = houses[house_name] + points
    print(points, " for ", house_name)
    return

def display_winning_house(houses):
    l1 = []
    max_points = -1
    house_winning = -1
    tie_house = -1
    for i in houses:
        l1.append(houses[i])
    for i in range(len(l1)):
        if l1[i] > max_points:
            max_points = l1[i]
            house_winning = i
    for i in range(len(l1)):
        if max_points == l1[i] and house_winning != i:
            tie_house = i
            break
    if house_winning == 0:
        house_winning = 'Gryffindor'
    elif house_winning == 1:
        house_winning = 'Slytherin'
    elif house_winning == 2:
        house_winning = 'Hufflepuff'
    elif house_winning == 3:
        house_winning = 'Ravenclaw'
    if tie_house == 0:
        tie_house = 'Gryffindor'
    elif tie_house == 1:
        tie_house = 'Slytherin'
    elif tie_house == 2:
        tie_house = 'Hufflepuff'
    elif tie_house == 3:
        tie_house = 'Ravenclaw'
        print("We have a tie, two houses winning", tie_house, "and", house_winning, "with a number of ", max_points,
              "points.")
    else:
        print("The winner is", house_winning, "with a number of ", max_points, "points.")
    return
