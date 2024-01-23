#!/usr/bin/env python3
import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANDOM_VALUE = random.randint(1, 300)


def is_prime(value):
    '''checks whether a number is prime or not'''
    if value == 1:
        return False
    for i in range(2, int(value / 2) + 1):
        if value % i == 0:
            return False
    return True


def get_question_answer():
    '''generates question and answer'''
    answer = 'yes' if is_prime(RANDOM_VALUE) else 'no'
    return [RANDOM_VALUE, answer]
