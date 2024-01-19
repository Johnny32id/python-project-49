#!/usr/bin/env python3
import random
import brain_games.check_yes_or_no

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_VALUE = random.randint(1, 100)


def is_even(value):
    return value % 2 == 0


def get_question_answer():
    answer = brain_games.check_yes_or_no.check(RANDOM_VALUE, is_even)
    return [RANDOM_VALUE, answer]
