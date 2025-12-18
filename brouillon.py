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