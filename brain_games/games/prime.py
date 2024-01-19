#!/usr/bin/env python3
import random
import brain_games.check_yes_or_no

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_VALUE = random.randint(1, 300)


def is_prime(value):
    for i in range(2, int(value / 2) + 1):
        if value % i == 0:
            return False
    return True


def get_question_answer():
    answer = brain_games.check_yes_or_no.check(RANDOM_VALUE, is_prime)
    return [RANDOM_VALUE, answer]
