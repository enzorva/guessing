import pyfiglet
import random

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
            print('Great! You have selected the Easy difficulty level.\nLets\'s start the game!\n')
            return 10
        elif choice == '2':
            print('Great! You have selected the Medium difficulty level.\nLets\'s start the game!\n')
            return 5
        elif choice == '3':
            print('Great! You have selected the Hard difficulty level.\nLets\'s start the game!\n')
            return 3
        else:
            print('Invalid choice. Please try again.\n')

def game_logic(chances):
    number_to_guess = random.randint(1, 100)
    while chances > 0:
        try:
            guess = int(input('Enter your guess: '))
            if guess < 1 or guess > 100:
                print('Please enter a number between 1 and 100.')
                continue
            if guess == number_to_guess:
                print('Congratulations! You guessed the correct number in {} chances!'.format(10 - chances + 1))
                break
            elif guess < number_to_guess:
                print('Incorrect! The number is greater than {}.\n'.format(guess))
            else:
                print('Too high! The number is less than {}.\n'.format(guess))
            chances -= 1
            if chances == 0:
                print(f'Sorry, you have no more chances left. The correct number was {number_to_guess}.')
        except ValueError:
            print('Invalid input. Please enter a valid number.')


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


main()