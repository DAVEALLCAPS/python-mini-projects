import random

perpetrators = [
    "Professor Eleanor Gray",
    "Detective Alex Turner",
    "Emma Brooks",
    "Chef Marco Rossi",
    "Dr. Samuel Clarke",
]

locations = ["Library", "Kitchen", "Garden", "Dining Room", "Study"]

weapons = ["Candlestick", "Knife", "Poison", "Revolver", "Rope"]

clues = {
    "Professor Eleanor Gray": {
        "confirm": [
            "You find a badge that belongs to a professor.",
            "The suspect seems very knowledgeable about the academic world.",
        ],
        "eliminate": [
            "The suspect seems to have no connection to academia.",
            "You find no evidence linking the professor to the crime.",
        ],
    },
    # ... (add confirm and eliminate clues for other perpetrators, locations, and weapons)
    "Library": {
        "confirm": [
            "A rare book is missing from the shelf.",
            "The dust on the floor has been recently disturbed.",
        ],
        "eliminate": [
            "The library appears to be in perfect order.",
            "There are no signs of any disturbance in the library.",
        ],
    },
    # ...
}


def get_clue(category, is_correct):
    if category in clues:
        clue_type = "confirm" if is_correct else "eliminate"
        if clues[category][clue_type]:
            return random.choice(clues[category][clue_type])
    return "No clues found here."


def print_list(options):
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")


def get_choice(options):
    print_list(options)
    choice = int(input("Choose a number: ")) - 1
    return options[choice]


def make_suggestion():
    print("Make a suggestion:")
    perpetrator = get_choice(perpetrators)
    location = get_choice(locations)
    weapon = get_choice(weapons)
    return perpetrator, location, weapon


def check_suggestion(perpetrator, location, weapon):
    correct = 0
    if perpetrator == true_perpetrator:
        correct += 1
    if location == true_location:
        correct += 1
    if weapon == true_weapon:
        correct += 1
    print(f"{correct} out of 3 are correct.")
    return correct


def make_accusation():
    print("Make an accusation! Be careful, you only get one shot at this.")
    perpetrator = get_choice(perpetrators)
    location = get_choice(locations)
    weapon = get_choice(weapons)
    return perpetrator, location, weapon


def check_accusation(perpetrator, location, weapon):
    if (perpetrator, location, weapon) == (
        true_perpetrator,
        true_location,
        true_weapon,
    ):
        print("Congratulations! You’ve solved the mystery.")
    else:
        print("Your accusation was incorrect. Game over.")
        print(
            f"The true perpetrator was {true_perpetrator} in the {true_location} with the {true_weapon}."
        )


def game_loop():
    while True:
        print("1: Make a suggestion")
        print("2: Make an accusation")
        print("3: Ask for a clue")
        choice = input("Choose an option: ")
        if choice == "1":
            suggestion = make_suggestion()
            check_suggestion(*suggestion)
        elif choice == "2":
            accusation = make_accusation()
            check_accusation(*accusation)
            break
        elif choice == "3":
            category = input("Ask for a clue about (perpetrator/location/weapon): ")
            is_correct = (
                category == true_perpetrator
                or category == true_location
                or category == true_weapon
            )
            print(get_clue(category, is_correct))
        else:
            print("Invalid option, please choose again.")


if __name__ == "__main__":
    true_perpetrator = random.choice(perpetrators)
    true_location = random.choice(locations)
    true_weapon = random.choice(weapons)
    print("Welcome to the Mystery Game!")
    game_loop()
