# Mystery Game

## Overview

Mystery Game is a text-based mini game where you take on the role of a detective trying to solve a mystery. Your goal is to determine the perpetrator, the location of the crime, and the weapon used. Throughout the game, you can make suggestions to gather information, make an accusation to solve the case, or ask for clues to help guide your investigation.

## Getting Started

1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Navigate to the directory containing the game script (`mystery_game.py`).
4. Run the script using Python:
   ```sh
   py mystery_game.py
   ```

## How to Play

Once the game starts, you will enter the main game loop where you have three options:

1. **Make a Suggestion**: Choose a perpetrator, location, and weapon from the given lists. The game will then tell you how many of your choices are correct.
2. **Make an Accusation**: Similar to making a suggestion, but be careful! You only get one chance to make an accusation. If you’re right, you win the game. If you’re wrong, the game is over.
3. **Ask for a Clue**: Request a clue about a specific perpetrator, location, or weapon. The clue may confirm if your suspicion is correct or eliminate an incorrect option.

To make a selection, simply input the number corresponding to your choice when prompted.

### Lists of Options

The game includes 5 options each for perpetrators, locations, and weapons.

#### Perpetrators:

1. Professor Eleanor Gray
2. Detective Alex Turner
3. Emma Brooks
4. Chef Marco Rossi
5. Dr. Samuel Clarke

#### Locations:

1. Library
2. Kitchen
3. Garden
4. Dining Room
5. Study

#### Weapons:

1. Candlestick
2. Knife
3. Poison
4. Revolver
5. Rope

## Game Flow

1. The game randomly selects a perpetrator, location, and weapon at the start.
2. You enter the game loop where you can make suggestions, accusations, or ask for clues.
3. Use the information gathered from suggestions and clues to form your accusation.
4. Make an accusation when you feel confident in your choices.
5. The game will end, revealing if your accusation was correct or not.

## Clues

Clues are designed to guide you in your investigation. There are two types of clues:

- **Confirming Clues**: These clues suggest that your suspicion about a certain option might be correct.
- **Eliminating Clues**: These clues suggest that a certain option is likely incorrect.

When asking for a clue, simply input the name of the category (perpetrator, location, or weapon) you want a clue about.

## Conclusion

Enjoy playing Mystery Game, and best of luck in solving the mystery! Remember, a good detective pays attention to detail and uses every piece of information available. Happy investigating!
