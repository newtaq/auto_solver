from openAI import get_openAI
import json


def solve(prompt: str, regenerate=False):
    with open("solving_saves.json", 'r') as rfile:
        data_solved = json.load(rfile)
    if regenerate is False and prompt in data_solved:
        return data_solved[prompt]
    else:
        # region chatGPT
        task = """Напиши решение задачи по физике (в формате {"Дано": %Дано%, "Найти": %Найти%, "Описание": %Описание%, "Формула": %Формула%, "Уравнение графика":%Уравнение 
        графика%, "Решение": %Решение%, "Ответ": %Ответ%}) используя формулы и пошаговые действия"""

        analyzed = get_openAI(task + prompt)
        try:
            analyzed_data = json.loads(analyzed)
            save_solve_into_json(prompt, analyzed_data)
            return analyzed_data
        except json.decoder.JSONDecodeError:
            return None
        # endregion


def create_json():
    with open("solving_saves.json", 'w') as wfile:
        json.dump({"None": None}, wfile)


def save_solve_into_json(prompt: str, analyzed_prompt: any):
    rfile = open("solving_saves.json", 'r')
    try:
        data = json.load(rfile)
    except AttributeError:
        create_json()
        save_solve_into_json(prompt, analyzed_prompt)
        return
    finally:
        rfile.close()

    data.update({prompt: analyzed_prompt})
    with open("solving_saves.json", 'w') as wfile:
        json.dump(data, wfile)
