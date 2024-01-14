#!/usr/bin/env python3
from brain_games.game import brain_game
from brain_games.games.calc import get_question_answer, RULE


def main():
    brain_game(get_question_answer, RULE)


if __name__ == '__main__':
    brain_game()
