import pyfiglet

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
            print('Great! You have selected the Easy difficulty level.\nLets\'s start the game!')
            return 10
        elif choice == '2':
            print('Great! You have selected the Medium difficulty level.\nLets\'s start the game!')
            return 5
        elif choice == '3':
            print('Great! You have selected the Hard difficulty level.\nLets\'s start the game!')
            return 3
        else:
            print('Invalid choice. Please try again.')


def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('Guessing Game'))
    print('''
          Welcome to the Number Guessing Game!
          I am thinking of a number between 1 and 100.
          You have 5 chances to guess the correct number.
          ''')

    difficulty = select_difficulty()
