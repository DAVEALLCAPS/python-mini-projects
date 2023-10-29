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
    "Perpetrators": {
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
        "Detective Alex Turner": {
            "confirm": [
                "You find a detective’s badge.",
                "The suspect has a strong understanding of crime scenes.",
            ],
            "eliminate": [
                "The suspect doesn’t seem to know much about investigative work.",
                "You can’t find any police equipment near the crime scene.",
            ],
        },
        "Emma Brooks": {
            "confirm": [
                "You find a woman’s purse at the crime scene.",
                "The suspect seems nervous and avoids eye contact.",
            ],
            "eliminate": [
                "The suspect has a solid alibi.",
                "You find no belongings of a woman at the crime scene.",
            ],
        },
        "Chef Marco Rossi": {
            "confirm": [
                "You find kitchen utensils near the crime scene.",
                "The suspect has a strong aroma of food.",
            ],
            "eliminate": [
                "The kitchen is in perfect order.",
                "You find no traces of food near the crime scene.",
            ],
        },
        "Dr. Samuel Clarke": {
            "confirm": [
                "You find medical supplies near the crime scene.",
                "The suspect has a calm and analytical demeanor.",
            ],
            "eliminate": [
                "The medical cabinet is locked and everything is accounted for.",
                "You find no evidence of medical knowledge in the suspect.",
            ],
        },
    },
    "Locations": {
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
        "Kitchen": {
            "confirm": [
                "The smell of recently cooked food lingers in the air.",
                "A knife is missing from the knife block.",
            ],
            "eliminate": [
                "The kitchen is spotless and everything is in its place.",
                "You find no signs of a struggle or disturbance.",
            ],
        },
        "Garden": {
            "confirm": [
                "Footprints lead through the garden.",
                "Some of the plants appear to be damaged.",
            ],
            "eliminate": [
                "The garden is well-maintained and shows no signs of disturbance.",
                "All footprints lead to normal places.",
            ],
        },
        "Dining Room": {
            "confirm": [
                "The table is set, but one seat is disheveled.",
                "A glass is broken on the floor.",
            ],
            "eliminate": [
                "The dining room is pristine and everything is in its place.",
                "The table settings are untouched.",
            ],
        },
        "Study": {
            "confirm": [
                "Papers are scattered about, as if someone was searching for something.",
                "The safe appears to have been tampered with.",
            ],
            "eliminate": [
                "The study is orderly and all papers are neatly stacked.",
                "The safe is securely locked.",
            ],
        },
    },
    "Weapons": {
        "Candlestick": {
            "confirm": [
                "You find candle wax at the crime scene.",
                "The candlestick is missing from its usual place.",
            ],
            "eliminate": [
                "You find no trace of candle wax anywhere near the crime scene.",
                "All candlesticks are accounted for.",
            ],
        },
        "Knife": {
            "confirm": [
                "You find a knife sheath, but no knife.",
                "The kitchen knife set is missing a knife.",
            ],
            "eliminate": [
                "All knives are accounted for.",
                "You find no signs of a knife being used at the crime scene.",
            ],
        },
        "Poison": {
            "confirm": [
                "You find an empty vial that smells of chemicals.",
                "The suspect has knowledge of toxic substances.",
            ],
            "eliminate": [
                "There are no signs of chemical substances at the crime scene.",
                "The medical supplies are all accounted for and securely stored.",
            ],
        },
        "Revolver": {
            "confirm": [
                "You find an empty shell casing.",
                "The suspect is known to have a firearm license.",
            ],
            "eliminate": [
                "There are no signs of gunfire.",
                "The suspect has a strong aversion to firearms.",
            ],
        },
        "Rope": {
            "confirm": [
                "You find a piece of frayed rope.",
                "The garden shed is missing a length of rope.",
            ],
            "eliminate": [
                "All ropes in the house are accounted for.",
                "You find no signs of rope being used in the crime.",
            ],
        },
    },
}


def get_clue(category, item, is_correct):
    if category in clues and item in clues[category]:
        clue_type = "confirm" if is_correct else "eliminate"
        if clues[category][item][clue_type]:
            return random.choice(clues[category][item][clue_type])
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
            print("1: Perpetrators")
            print("2: Locations")
            print("3: Weapons")
            category_choice = input("Choose a category for the clue: ")
            if category_choice == "1":
                category = "Perpetrators"
                options = perpetrators
            elif category_choice == "2":
                category = "Locations"
                options = locations
            elif category_choice == "3":
                category = "Weapons"
                options = weapons
            else:
                print("Invalid option. Returning to main menu.")
                continue
            item = get_choice(options)
            is_correct = item in [true_perpetrator, true_location, true_weapon]
            print(get_clue(category, item, is_correct))
        else:
            print("Invalid option, please choose again.")


if __name__ == "__main__":
    true_perpetrator = random.choice(perpetrators)
    true_location = random.choice(locations)
    true_weapon = random.choice(weapons)
    print("Welcome to the Mystery Game!")
    game_loop()
