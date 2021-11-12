import random

def main():
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
                # and points are unequal to the length of the computer guess, guesses is increased by 1. current points are
                # then calculated using the check word function with the command and previous points

                command = input(
                    f'Guess a letter of a {len(computer_guess)} letter word.\nYou have {guess_limit} guesses.\n>').lower()

                while points <= len(computer_guess):
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
                    command = input(f'What does {num1} to the power of {num2} equal? > ')

                    if int(command) == answer:
                        print('You are correct!')
                    elif int(command) != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '2':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 / num2
                    command = input(f'What does {num1} divided by {num2} equal? > ')

                    if float(command) == answer:
                        print('You are correct!')
                    elif float(command) != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '3':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 % num2
                    command = input(f'What is the remainder of {num1} divided by {num2}? > ')

                    if int(command) == answer:
                        print('You are correct!')
                    elif int(command) != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '4':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 // num2
                    command = int(input(f'How many full times does {num2} go into {num1}? > '))

                    if int(command) == answer:
                        print('You are correct!')
                    elif int(command) != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == '5':
                    num1 = random.choice(numbers)
                    num2 = random.choice(numbers)
                    answer = num1 - num2
                    command = int(input(f'What is {num1} minus {num2}? > '))

                    if int(command) == answer:
                        print('You are correct!')
                    elif int(command) != answer:
                        print(f'Your answer is incorrect.\nThe answer is {answer}')

                elif command == "help":
                    print('stop - to stop the game\nhelp - to show instructions\nquit - to exit')

                elif command == 'stop':
                    math_started = False
                    print("Math stopped.")
                    command = input(">").lower()

                else:
                    print('WHAT?????')
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

                    startNum = int(input('Enter a starting number: '))
                    endingNum = int(input('Enter a ending number: '))
                    multiple = int(input('Enter a multiple: '))

                    if endingNum % multiple == 0:
                        for number in range(startNum, endingNum + 1, multiple):
                            print(number)

                    elif endingNum % multiple != 0:
                        print(f'{multiple} isnt a multiple of {endingNum}')

                    else:
                        print('What bruh??')
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

        elif command == "quit" or "leave":
            print("Ok. Shutting down.")
            stop_game = True
            break

        else:
            print('WHAT???')
            command = input(">").lower()


# function to check the users guess against each letter in the word chosen by the computer.
# If it matches, you gain a point. If it doesnt, you dont.


def check_word(user_guess, points, computer_guess):
    letter = 0
    while letter != len(computer_guess):
        for x in computer_guess:
            letter = letter + 1
            if x == user_guess:
                points = points + 1
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
      'misc - to start misc, functions', 'stop - to stop the game', 'help - to show instructions',
      'quit - to exit', sep='\n')


main()