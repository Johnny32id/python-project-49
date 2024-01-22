#!/usr/bin/env python3
import random

RULE = 'What is the result of the expression?'


def get_random_sign(signs):
    '''returns a random sign from the passed arguments'''
    random_index = random.randint(0, len(signs) - 1)
    return signs[random_index]


def calculate(first_value, second_value, sign):
    '''calculates the result of addition, subtraction or multiplication
    depending on the passed sign'''
    match sign:
        case '+':
            return first_value + second_value
        case '-':
            return first_value - second_value
        case _:
            return first_value * second_value


def get_question_answer():
    '''generates question and answer'''
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    random_sign = get_random_sign(['+', '-', '*'])
    question = f"{first_value} {random_sign} {second_value}"
    answer = str(calculate(first_value, second_value, random_sign))
    return [question, answer]
