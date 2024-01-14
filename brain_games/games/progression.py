#!/usr/bin/env python3
import random
from brain_games.game import brain_game

RULE = 'What number is missing in the progression?'
PROGRESSION_LENGTH = random.randint(5, 10)


def get_question(first_value, difference, value_to_skip):
    progression = ''
    counter = 0
    while counter < PROGRESSION_LENGTH:
        if counter == value_to_skip:
            progression = progression + '.. '
            counter += 1
            continue
        progression_value = first_value + difference * counter
        progression = progression + f'{progression_value} '
        counter += 1
    return progression.strip()


def get_question_answer():
    first_value = random.randint(2, 50)
    difference = random.randint(2, 5)
    value_to_skip = random.randint(0, PROGRESSION_LENGTH - 1)
    question = get_question(first_value, difference, value_to_skip)
    answer = str(first_value + difference * value_to_skip)
    return [question, answer]


def progression_game():
    brain_game(get_question_answer, RULE)
