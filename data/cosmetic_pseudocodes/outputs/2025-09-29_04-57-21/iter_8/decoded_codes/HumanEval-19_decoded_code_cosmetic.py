from typing import List


def sort_numbers(string_of_number_words: str) -> str:
    digit_values: dict[str, int] = {
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

    filtered_words: List[str] = []
    current_index = 0
    all_words = string_of_number_words.split(' ')

    while current_index < len(all_words):
        candidate_word = all_words[current_index]
        if candidate_word != '':
            filtered_words.append(candidate_word)
        current_index += 1

    def compare_func(a: str, b: str) -> int:
        return 1 if digit_values[a] >= digit_values[b] else -1

    sorted_result = filtered_words[:]

    i = 0
    while i < len(sorted_result):
        j = i + 1
        while j < len(sorted_result):
            if compare_func(sorted_result[i], sorted_result[j]) > 0:
                sorted_result[i], sorted_result[j] = sorted_result[j], sorted_result[i]
            j += 1
        i += 1

    joined_string = ''
    idx = 0
    while idx < len(sorted_result):
        joined_string += sorted_result[idx]
        if idx < len(sorted_result) - 1:
            joined_string += ' '
        idx += 1

    return joined_string