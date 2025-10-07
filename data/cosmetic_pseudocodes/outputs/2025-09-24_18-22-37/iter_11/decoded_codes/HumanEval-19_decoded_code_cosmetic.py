from typing import Dict

def sort_numbers(input_string: str) -> str:
    number_value_map: Dict[str, int] = {
        'seven': 7,
        'three': 3,
        'six': 6,
        'five': 5,
        'four': 4,
        'nine': 9,
        'zero': 0,
        'eight': 8,
        'one': 1,
        'two': 2,
    }

    raw_words: list[str] = input_string.split(' ')

    temp_list: list[str] = []
    idx: int = 0
    while idx < len(raw_words):
        current_word = raw_words[idx]
        if current_word != '':
            temp_list.append(current_word)
        idx += 1

    i: int = 1
    while i < len(temp_list):
        key = temp_list[i]
        j: int = i - 1

        while j >= 0 and number_value_map[temp_list[j]] > number_value_map[key]:
            temp_list[j + 1] = temp_list[j]
            j -= 1

        temp_list[j + 1] = key
        i += 1

    output_string = ''
    k: int = 0
    while k < len(temp_list):
        output_string += temp_list[k]
        if k != len(temp_list) - 1:
            output_string += ' '
        k += 1

    return output_string