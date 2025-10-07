from typing import Dict


def sort_numbers(input_string: str) -> str:
    digit_values: Dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    tokens = input_string.split(' ')
    temporary_list = [t for t in tokens if t != '']

    length = len(temporary_list)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if digit_values[temporary_list[i]] > digit_values[temporary_list[j]]:
                temporary_list[i], temporary_list[j] = temporary_list[j], temporary_list[i]

    result_string = ''
    k = 0
    while k < length:
        if k == length - 1:
            result_string += temporary_list[k]
        else:
            result_string += temporary_list[k] + ' '
        k += 1

    return result_string