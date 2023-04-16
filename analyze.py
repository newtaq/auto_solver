from re import sub
import json
from string import digits
from pymorphy3 import MorphAnalyzer

# region config
with open("CONFIG.json", 'r') as rfile:
    CONFIG: dict = json.load(rfile)

print(CONFIG)


# endregion

def str_to_num(num_str: str) -> int | float | str:
    try:
        num_str = float(num_str)
        if int(num_str) == num_str:
            num_str = int(num_str)
    finally:
        return num_str

def dict_get_key(d: dict, val):
    key_list = list(d.keys())
    val_list = list(d.values())
    try:
        pos = val_list.index(val)
        return key_list[pos]
    except ValueError:
        return None

def get_data_from_text(inp_str):
    def measureParser(mes_str: str):
        mes_out = ''
        mult = 1
        for mes_part in mes_str.split('/'):
            for pref in CONFIG['PREFIXES']:
                if mes_part.find(pref) == 0 and pref != mes_part:
                    mes_part = mes_part.replace(pref, '', 1)
                    mult *= CONFIG['PREFIXES'][pref]
                    break
                elif mes_part in CONFIG['PREFIXES_WORDS']:
                    mes_part = CONFIG['PREFIXES_WORDS'][mes_part][0]
                    mult *= CONFIG['PREFIXES_WORDS'][mes_part][1]
                    break
            mes_out += f'{mes_part}/'
        return mes_out[:len(mes_out) - 1], mult

    def isMeasure(mes_str: str) -> bool:
        if isinstance(mes_str, tuple):
            mes_str = mes_str[0]
        for m in CONFIG['TITLES'].values():
            if m == mes_str:
                return True
        else:
            return False

    inp_str = inp_str
    PATTERN_TO_DEL = '[&|?|!|(|)]'
    inp_str = sub(PATTERN_TO_DEL, '', inp_str.replace(', ', ' '))
    cur_mode = 'GIVEN'
    data_list = []
    i = 0
    for word in inp_str.split():
        if isinstance(converted_num := str_to_num(word), int | float):
            data_list += [converted_num]
        else:
            morphed_world = MorphAnalyzer().normal_forms(word)[0]
            for mes_word in CONFIG["MEASURE_WORD"]:
                if mes_word in morphed_world:
                    morphed_world = morphed_world.replace(mes_word, CONFIG["MEASURE_WORD"][mes_word])

            word = word[0] + morphed_world[1:]
            parsed_word, mult = measureParser(word)
            if isMeasure(parsed_word):
                data_list += [parsed_word]
                if i >= 1 and isinstance(data_list[i - 1], int | float):
                    data_list[i - 1] *= mult
            else:
                if cur_mode == 'GIVEN' and word in CONFIG['BASIC']:
                    cur_mode = CONFIG['BASIC'][wordr
                if morphed_world in list(CONFIG["BASIC"].keys()) + list(CONFIG["TITLES"].keys()) + list(CONFIG["BASIC"].values()):
                    data_list += [morphed_world]
                else:
                    i -= 1
        i += 1

    cur_mode = 'GIVEN'
    data_dict = {"GIVEN": {}, "FIND": {}}
    i = 0
    while i < len(data_list):
        word = data_list[i]
        if word in CONFIG['BASIC']:
            cur_mode = CONFIG['BASIC'][word]
        elif cur_mode == 'GIVEN':
            if i + 1 < len(data_list) and isinstance(word, int | float) and data_list[i + 1] in CONFIG['TITLES'].values():
                data_dict[cur_mode][dict_get_key(CONFIG["TITLES"], data_list[i+1])] = {"VALUE": word, "MEASURE": data_list[i + 1]}
            elif word in CONFIG['TITLES']:
                if data_list[i+1] in
        i += 1
    print(data_list)
    print(data_dict)


if __name__ == '__main__':
    get_data_from_text('Найти с какой скоростью проезжает если машина 10 за время 10 секунд')
