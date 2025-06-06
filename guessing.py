import pyfiglet
import random
import sys
import time
import csv

def select_difficulty():
    print('''
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
''')
    while True:
        choice = input('Enter your choice: ')
        if choice == '1':
            print('\nGreat! You have selected the Easy difficulty level.\nLets\'s start the game!\n')
            return 10
        elif choice == '2':
            print('\nGreat! You have selected the Medium difficulty level.\nLets\'s start the game!\n')
            return 5
        elif choice == '3':
            print('\nGreat! You have selected the Hard difficulty level.\nLets\'s start the game!\n')
            return 3
        else:
            print('\nInvalid choice. Please try again.\n')

def game_logic(chances):
    number_to_guess = random.randint(1, 100)
    start_time = time.time()
    total_chances = chances
    success = False

    hint = input('Do you want a hint? (y/n): ').lower()
    if hint == 'y':
        if number_to_guess % 2 == 0:
            print('Hint: The number is even.\n')
        else:
            print('Hint: The number is odd.\n')
    elif hint == 'n':
        print('\n')
    else:
        print('Invalid choice. No hint provided.\n')

    while chances > 0:
        try:
            guess = int(input('Enter your guess: '))
            if guess < 1 or guess > 100:
                print('Please enter a number between 1 and 100.')
                continue
            if guess == number_to_guess:
                end_time = time.time()
                elapsed_time = end_time - start_time
                attempts = total_chances - chances + 1
                print('Congratulations! You guessed the correct number in {} attemps!\n'.format(attempts))
                print(f'You took {elapsed_time:.2f} seconds to play the game.\n')
                success = True
                break
            elif guess < number_to_guess:
                print('Incorrect! The number is greater than {}.\n'.format(guess))
            else:
                print('Too high! The number is less than {}.\n'.format(guess))
            chances -= 1
        except ValueError:
            print('Invalid input. Please enter a valid number.\n')

    if not success:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Sorry, you have no more chances left. The correct number was {number_to_guess}.\n')
        print(f'You took {elapsed_time:.2f} seconds to play the game.\n')

    save_results_to_csv(success, attempts, elapsed_time, number_to_guess)

def save_results_to_csv(success, attempts, elapsed_time, number_to_guess):
    with open('game_results.csv', mode='a+', newline='') as file:
        writer = csv.writer(file)

        file.seek(0)
        if not file.read(1):
            writer.writerow(['Success', 'Attempts', 'Elapsed Time (seconds)', 'Number to Guess'])

        writer.writerow(['Yes' if success else 'No', attempts if success else 'N/A', f'{elapsed_time:.2f}', number_to_guess])

def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('Guessing Game'))
    print('''
Welcome to the Number Guessing Game!
I am thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.
''')

    difficulty = select_difficulty()
    game_logic(difficulty)
    play_again = input('Want to play again? (y/n): ').lower()
    if play_again == 'y':
        main()
    elif play_again == 'n':
        print('Thanks for playing! Goodbye!\n')
        sys.exit()
    else:
        print('Invalid choice. Exiting the game.\n')
        sys.exit()


main()