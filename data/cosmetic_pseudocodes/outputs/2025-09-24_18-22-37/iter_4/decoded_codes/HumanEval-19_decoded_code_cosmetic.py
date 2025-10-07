from typing import Callable

def sort_numbers(number_words_string: str) -> str:
    mapping_dictionary: dict[str, int] = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    words_array: list[str] = []
    index: int = 0
    temp_words = number_words_string.split(' ')
    while index < len(temp_words):
        if temp_words[index] != '':
            words_array.append(temp_words[index])
        index += 1

    def ordering_function(a: str, b: str) -> int:
        if mapping_dictionary[a] < mapping_dictionary[b]:
            return -1
        elif mapping_dictionary[a] > mapping_dictionary[b]:
            return 1
        else:
            return 0

    # Since Python's sort doesn't support cmp directly, use cmp_to_key
    from functools import cmp_to_key
    words_array.sort(key=cmp_to_key(ordering_function))

    result_string = ''
    pos = 0
    while pos < len(words_array):
        if pos == 0:
            result_string = words_array[pos]
        else:
            result_string = result_string + ' ' + words_array[pos]
        pos += 1

    return result_string