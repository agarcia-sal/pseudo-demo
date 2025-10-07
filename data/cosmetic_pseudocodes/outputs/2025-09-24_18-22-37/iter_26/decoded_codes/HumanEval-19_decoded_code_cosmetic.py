from typing import Dict


def sort_numbers(string_of_number_words: str) -> str:
    lookup_table: Dict[str, int] = {
        'zero': 0x0,
        'one': 0x1,
        'two': 0x2,
        'three': 0x3,
        'four': 0x4,
        'five': 0x5,
        'six': 0x6,
        'seven': 0x7,
        'eight': 0x8,
        'nine': 0x9,
    }

    raw_tokens = string_of_number_words.split(' ')
    filtered_tokens = []
    current_index = 0
    while current_index < len(raw_tokens):
        candidate = raw_tokens[current_index]
        if candidate != '':
            filtered_tokens.append(candidate)
        current_index += 1

    temp_sorted = filtered_tokens[:]

    i = 1
    while i < len(temp_sorted):
        j = i
        while (
            j > 0
            and lookup_table[temp_sorted[j]] < lookup_table[temp_sorted[j - 1]]
        ):
            temp = temp_sorted[j]
            temp_sorted[j] = temp_sorted[j - 1]
            temp_sorted[j - 1] = temp
            j -= 1
        i += 1

    result_string = ''
    k = 0
    if len(temp_sorted) == 0:
        return result_string

    while True:
        result_string += temp_sorted[k]
        k += 1
        if k == len(temp_sorted):
            break
        result_string += ' '

    return result_string