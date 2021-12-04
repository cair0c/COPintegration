"""Integration Project. Multiple functions including hangman, math, and misc. functions"""
__author__ = "Cairo"

import random


def main():
    """This is the main encompassing function which includes  all of the functionality of the program. Beginning with
    the hangman game, followed by the math section, and lastly the misc. functions."""

    game_started = False
    stop_game = False
    math_started = False
    misc_started = False

    dictionary = ['able', 'about', 'account', 'acid', 'across', 'act']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    command = input(">").lower()

    while not stop_game:

        if command == "help":
            print('hangman - to start the Hangman\nmath - to start the math game\nstop - to stop the game\nhelp - to'
                  ' show instructions\nquit - to exit')
            command = input(">").lower()

        # Hangman portion

        elif command == "hangman":
            if game_started:
                print('The game is already started.')
            else:
                print("Game started!")
                game_started = True
                computer_guess = random.choice(dictionary)
                guess_limit = len(computer_guess) * 2

            while game_started:
                guesses = 0
                points = 0

                # when the length of command is 1 letter, the amount of guesses left is less than or equal to the limit,
                # and points are unequal to the length of the computer guess, guesses is increased by 1. current points
                # are then calculated using the check word function with the command and previous points

                command = input(
                    f'Guess a letter of a {len(computer_guess)} letter word.\nYou have {guess_limit} guesses.\n>'
                ).lower()

                while points < len(computer_guess):
                    if len(command) == 1 and guesses != guess_limit:
                        guesses += 1
                        points = check_word(command, points, computer_guess)
                        print(f'You have {points} out of {len(computer_guess)} points!')
                        print(f'You have {guess_limit - guesses} guesses left.')
                        command = input(">").lower()
                    elif guesses == guess_limit:
                        print('You are out of guesses.\nRestart the game.')
                        game_started = False
                        command = input(">").lower()
                    else:
                        print('WHAT???')
                        command = input(">").lower()
                else:
                    print('You Won!\nRestart the game. ')
                    game_started = False
                    command = input(">").lower()

                if command == 'stop':
                    if game_started:
                        print("Game stopped.")
                        game_started = False
                    elif not game_started:
                        print('The game is already stopped.')
                    command = input(">").lower()

                else:
                    print('WHAT???')
                    command = input(">").lower()

        # Math portion

        elif command == 'math':
            print('Welcome to' + ' Math' * 10)
            math_started = True

            while math_started:

                print('Choose a problem')
                print('1. Exponents', '2. Division', '3. Remainder', '4. Floor division', '5. Subtraction', sep='\n')
                command = input('> ').lower()

                if command == '1':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 ** num2

                    while True:
                        try:
                            command = int(input(f'What does {num1} to the power of {num2} equal? > '))
                            break
                        except ValueError:
                            print('Input should be a number.')

                    if command == answer:
                        print('You are correct!')
                    elif command != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '2':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 / num2

                    while True:
                        try:
                            command = float(input(f'What does {num1} divided by {num2} equal? > '))
                            break
                        except ValueError:
                            print('Input should be a number.')

                    if command == answer:
                        print('You are correct!')
                    elif command != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '3':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 % num2

                    while True:
                        try:
                            command = int(input(f'What is the remainder of {num1} divided by {num2}? > '))
                            break
                        except ValueError:
                            print('Input should be a number.')

                    if command == answer:
                        print('You are correct!')
                    elif command != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '4':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 // num2

                    while True:
                        try:
                            command = int(input(f'How many full times does {num2} go into {num1}? > '))
                            break
                        except ValueError:
                            print('Input should be a number.')

                    if command == answer:
                        print('You are correct!')
                    elif command != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '5':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 - num2

                    while True:
                        try:
                            command = int(input(f'What is {num1} minus {num2}? > '))
                            break
                        except ValueError:
                            print('Input should be a number.')

                    if command == answer:
                        print('You are correct!')
                    elif command != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == "help":
                    print('stop - to stop the game\nhelp - to show instructions\nquit - to exit')

                elif command == 'stop':
                    math_started = False
                    print("Math stopped.")
                    command = input(">").lower()

                else:
                    print('WHAT??? Input should be a number from the list.')
                    command = input(">").lower()

        # Misc portion

        elif command == "misc":
            print('Welcome to Misc. functions')
            misc_started = True

            while misc_started:

                print('Choose a problem')
                print('1. Multiple Printer')

                command = input(">").lower()

                if command == '1':
                    while True:
                        try:
                            start_num = int(input('Enter a starting number: '))
                            ending_num = int(input('Enter a ending number: '))
                            multiple = int(input('Enter a multiple: '))
                            break
                        except ValueError:
                            print('Input should be a number.')

                    if ending_num % multiple == 0:
                        for number in range(start_num, ending_num + 1, multiple):
                            print(number)

                    elif ending_num % multiple != 0:
                        print(f"{multiple} isn't a multiple of {ending_num}")

                    else:
                        print('WHAT???')
                        command = input(">").lower()

                else:
                    print('WHAT?????')

        elif command == "stop":
            if game_started:
                print("Game stopped.")
                game_started = False
            elif not game_started:
                print('The game is already stopped.')
            command = input(">").lower()

        elif command == "quit":
            print("Ok. Shutting down.")
            stop_game = True
            break

        else:
            print('WHAT??? Input should be a choice from the list.')
            command = input(">").lower()


# function to check the users guess against each letter in the word chosen by the computer.
# If it matches, you gain a point. If it doesnt, you don't.


def check_word(user_guess, points, computer_guess):
    """The purpose of this function is to take in the letter guessed by the user, the amount of accumulated points, and
    the computer guess, then iterate through the computer guess to determine if the letter guessed by the user is in the
    word chosen by the computer. If the letter is a match, then a point is added, if not then it is skipped. Once it is
    done, it returns the new number of points"""

    letter = 0
    while letter != len(computer_guess):
        for x in computer_guess:
            letter += 1
            if x == user_guess:
                points += 1
                print(f'you guessed letter {letter} correct!')
            elif x != user_guess:
                print(f'you guessed letter {letter} wrong')
            else:
                continue
    return points


print('''
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝''')
print("Written by:")
print(''' ______     ______     __     ______     ______    
/\  ___\   /\  __ \   /\ \   /\  == \   /\  __ \   
\ \ \____  \ \  __ \  \ \ \  \ \  __<   \ \ \/\ \  
 \ \_____\  \ \_\ \_\  \ \_\  \ \_\ \_\  \ \_____\ 
  \/_____/   \/_/\/_/   \/_/   \/_/ /_/   \/_____/''')
print('\nInstructions', 'hangman - to start the Hangman', 'math - to start the math game',
      'misc - to start misc functions', 'stop - to stop the game', 'help - to show instructions',
      'quit - to exit', sep='\n')

main()
