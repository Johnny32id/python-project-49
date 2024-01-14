#!/usr/bin/env python3
import random
from brain_games.game import brain_game

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(value):
    if value <= 1:
        return False
    elif value > 1:
        for i in range(2, int(value / 2) + 1):
            if value % i == 0:
                return False
    return True


def get_question_answer():
    question = random.randint(1, 300)
    answer = 'yes' if is_prime(question) else 'no'
    return [question, answer]


def prime_game():
    brain_game(get_question_answer, RULE)
