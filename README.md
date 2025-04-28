# Number Guessing Game

Welcome to the **Number Guessing Game**! This is a fun and interactive Python-based game where you try to guess a randomly generated number within a limited number of attempts. The game also includes a hint system and tracks your performance by saving results to a CSV file.

## Features
- **Difficulty Levels**: Choose from Easy, Medium, or Hard difficulty levels, each with a different number of attempts.
- **Hint System**: Get hints about whether the number is even or odd.
- **Performance Tracking**: The game saves your results (success/failure, number of attempts, and time taken) to a CSV file for future reference.
- **Replay Option**: Play the game as many times as you like.

## How to Play
1. Run the Python script.
2. Select a difficulty level:
   - Easy: 10 attempts
   - Medium: 5 attempts
   - Hard: 3 attempts
3. Guess the number between 1 and 100.
4. Use the hint system if needed by typing `y` when prompted.
5. Your results will be saved to a CSV file named `game_results.csv`.

## Requirements
- Python 3.x
- The following Python modules:
  - `pyfiglet`
  - `random`
  - `sys`
  - `time`
  - `csv`

## Installation
1. Clone this repository or download the script.
2. Install the required Python modules using pip:
   ```bash
   pip install pyfiglet
   ```
3. Run the script:
   ```bash
   python guessing.py
   ```

## Example Output
```
Guessing Game
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2
Great! You have selected the Medium difficulty level.
Lets's start the game!

Do you want a hint? (y/n): y
Hint: The number is odd.

Enter your guess: 50
Too high! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 37
Congratulations! You guessed the correct number in 3 attempts!
You took 12.45 seconds to play the game.
```

## Project Inspiration
This project was inspired by the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) on roadmap.sh.