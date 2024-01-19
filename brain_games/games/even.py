#!/usr/bin/env python3
import random
import brain_games.check_yes_or_no

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(value):
    return value % 2 == 0


def get_question_answer():
    question = random.randint(1, 100)
    answer = brain_games.check_yes_or_no.check(question, is_even)
    return [question, answer]
