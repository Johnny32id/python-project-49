import prompt


def brain_game(get_question_anser, rule):
    print('Welcome to the Brain Games!')
    USER_NAME = prompt.string('May I have your name? ')
    print(f"Hello, {USER_NAME}!")
    print(rule)
    questions_quantity = 0
    while questions_quantity < 3:
        question_answer = get_question_anser()
        correct = question_answer[1]
        print(f"Question:{question_answer[0]}")
        answer = prompt.string('Your answer: ')
        if answer == correct:
            print('Correct!')
            questions_quantity += 1
            continue
        print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct}".')
        print(f'Let\'s try again, {USER_NAME}!')
        return
    print(f"Congratulations, {USER_NAME}!")
