#!/usr/bin/env python3
import random
import math
from brain_games.game import brain_game

RULE = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    question = f"{first_value} {second_value}"
    answer = str(math.gcd(first_value, second_value))
    return [question, answer]


def main():
    brain_game(get_question_answer, RULE)


if __name__ == '__main__':
    main()
