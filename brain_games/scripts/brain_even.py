#!/usr/bin/env python3
import prompt
import random


def main():
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        value = random.randint(1, 100)
        correct = 'yes' if value % 2 == 0 else 'no'
        print(f"Question:{value}")
        answer = prompt.string('Your answer:')
        if answer == correct:
            print('Correct!')
            counter += 1
            continue
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct}".')
        print(f'Let\'s try again, {user_name}!')
        return
    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    main()
