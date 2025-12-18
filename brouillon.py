def assign_house(character, questions):
    questions = [
        (
            "You see a friend in danger. What do you do?",
            ["Rush to help", "Think of a plan", "Seek help", "Stay calm and observe"],
             ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),
        ("Which trait describes you best?",
            ["Brave and loyal", "Cunning and ambitious", "Patient and hardworking", "Intelligent and curious"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]),
        ("When faced with a difficult challenge, you...",
            ["Charge in without hesitation", "Look for the best strategy", "Rely on your friends","Analyze the problem"],
            ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"])]
    for i in questions:
        print(i)
a = assign