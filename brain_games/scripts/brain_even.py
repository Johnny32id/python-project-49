#!/usr/bin/env python3
import random
from brain_games.game import brain_game

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return value % 2 == 0


def get_question_answer():
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return [question, answer]


def main():
    brain_game(get_question_answer, RULE)


if __name__ == '__main__':
    main()
