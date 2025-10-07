from typing import Dict, List


def sort_numbers(input_string: str) -> str:
    mapping: Dict[str, int] = {
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

    temp_words: List[str] = []
    words: List[str] = input_string.split(' ')
    n: int = len(words)
    index: int = 0
    while index < n:
        current_word: str = words[index]
        if current_word != '':
            temp_words.append(current_word)
        index += 1

    result_list: List[str] = temp_words.copy()
    i: int = 1
    while i < len(result_list):
        j: int = 0
        while j < len(result_list) - i:
            left_value: int = mapping[result_list[j]]
            right_value: int = mapping[result_list[j + 1]]
            if left_value > right_value:
                temp: str = result_list[j]
                result_list[j] = result_list[j + 1]
                result_list[j + 1] = temp
            j += 1
        i += 1

    output_string: str = ''
    k: int = 0
    length_result: int = len(result_list)
    while k < length_result:
        if k == length_result - 1:
            output_string += result_list[k]
        else:
            output_string += result_list[k] + ' '
        k += 1

    return output_string