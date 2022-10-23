import json


def load_candidates():
    '''Загрузка содержимого файла с кандидатами'''

    with open('candidates.json', encoding='utf-8') as file:
        file_content = json.loads(file.read())
    return file_content


def get_all():
    '''Возвращает список всех кандидатов в необходимом формате'''

    file_content = load_candidates()
    candidates_str = ''

    for item in file_content:
        candidates_str += f'<pre>Имя кандидата: {item["name"]}\n' \
                          f'Позиция кандидата: {item["position"]}\n' \
                          f'Навыки кандидата: {item["skills"]}\n' \
                          f'\n</pre>'

    return candidates_str


def get_by_pk(pk):
    '''Возвращает кандидата по его номеру в списке'''

    file_content = load_candidates()
    candidates_str = ''

    for item in file_content:
        if int(pk) == item['pk']:
            url = item['picture']
            candidates_str += f"<img src='{url}'>"
            candidates_str += f'<pre>Имя кандидата: {item["name"]}\n' \
                              f'Позиция кандидата: {item["position"]}\n' \
                              f'Навыки кандидата: {item["skills"]}\n' \
                              f'\n</pre>'

    if candidates_str:
        return candidates_str
    else:
        return 'Такого кандидата нет'


def get_by_skill(skill_name):
    '''Возвращает кандидатов по их навыкам'''

    file_content = load_candidates()
    candidates_str = ''

    for item in file_content:
        # нужный навык и навык кандидата переводятся в нижний регистр
        if skill_name.lower() in [x.lower() for x in item['skills'].split(', ')]:
            candidates_str += f'<pre>Имя кандидата: {item["name"]}\n' \
                              f'Позиция кандидата: {item["position"]}\n' \
                              f'Навыки кандидата: {item["skills"]}\n' \
                              f'\n</pre>'

    if candidates_str:
        return candidates_str
    else:
        return 'Такого кандидата нет'
