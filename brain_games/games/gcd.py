#!/usr/bin/env python3
import random
RULE = 'Find the greatest common divisor of given numbers.'


def gcd(x, y):
    '''finds the greatest common divisor'''
    while (y):
        x, y = y, x % y
    return x


def get_question_answer():
    '''generates question and answer'''
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    question = f"{first_value} {second_value}"
    answer = str(gcd(first_value, second_value))
    return [question, answer]
