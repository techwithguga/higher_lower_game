# Higher-Lower Terminal Game

This is a terminal-based game built in Python. In this game, players are presented with two social media accounts and must guess which account has more followers. The game continues until the player makes an incorrect guess.

## Features

- Displays two social media accounts with their respective follower counts.
- Allows the player to guess which account has more followers by typing 'A' or 'B'.
- Feedback on the user guess.
- Keeps track of the player's score.
- Uses ASCII art for a visually appealing interface.

## How to Play

1. Run the Python script in your terminal.
2. You will be presented with two social media accounts with their follower counts.
3. Guess which account has more followers by typing 'A' or 'B' and pressing enter.
4. Receive feedback of your guess.
5. If your guess is correct, your score will increase, and the game will continue with a new set of accounts.
6. If your guess is incorrect, the game will end, and your final score will be displayed.

## Dependencies

- `art`: This package is used to generate ASCII art for the game's logo, versus symbol, and feedback messages.
- `game_data`: This file contains the data (social media account information) used in the game.
- `random`: This module is used to randomly select social media accounts for each round of the game.
- `replit`: This package is used to clear the terminal screen after each round of the game.

## How to Run

1. Clone this repository to your local machine.
2. Install the required dependencies (`art` and `replit`) using pip.
3. CD `higher_lower_game` Run the Python script `main.py` in your terminal.
4. Follow the on-screen instructions to play the game.

## Demo

A live demo of the game can be found [here](https://replit.com/@gukh/higherlowergame).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
