#!/usr/bin/env python3
import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
RANDOM_VALUE = random.randint(1, 100)


def is_even(value):
    '''checking numbers for parity'''
    return value % 2 == 0


def get_question_answer():
    '''generates question and answer'''
    answer = 'yes' if is_even(RANDOM_VALUE) else 'no'
    return [RANDOM_VALUE, answer]
