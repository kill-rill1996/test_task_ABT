import json
import argparse
import sys


def get_data_from_json(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    count_questions_in_rounds = [len(round['questions']) for round in data['game']['rounds']]
    print(f'Суммарное количество вопрос в игре: {sum(count_questions_in_rounds)}')


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    correct_answers = []
    for round_questions in [round['questions'] for round in data['game']['rounds']]:
        for question in round_questions:
            correct_answers.append(question['correct_answer'])
    print(f'Правильные ответы для игры: {correct_answers}')


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    # если время на ответ не указана в вопросе, используется время из настроек раунда

    times_to_answers = []

    for round in [round for round in data['game']['rounds']]:
        for question in round['questions']:
            time_to_answer = question.get('time_to_answer', 0)
            if time_to_answer:
                times_to_answers.append(time_to_answer)
            else:
                times_to_answers.append(round['settings']['time_to_answer'])
    print(f'Максимальное время на ответ в игре: {max(times_to_answers)}')


def main(file):
    data = get_data_from_json(file)     # загрузить данные из test.json файла

    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get JSON file and returns some information.')
    parser.add_argument('-file', nargs='?', help='name of json file')
    namespace = parser.parse_args(sys.argv[1:])
    main(file=namespace.file)
