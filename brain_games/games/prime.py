#!/usr/bin/env python3
import random
import brain_games.check_yes_or_no

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(value):
    for i in range(2, int(value / 2) + 1):
        if value % i == 0:
            return False
    return True


def get_question_answer():
    question = random.randint(1, 300)
    answer = brain_games.check_yes_or_no.check(question, is_prime)
    return [question, answer]
