from typing import List


def sort_numbers(input_sequence: str) -> str:
    mapping_dict: dict[str, int] = {
        'nine': 9,
        'eight': 8,
        'seven': 7,
        'six': 6,
        'five': 5,
        'four': 4,
        'three': 3,
        'two': 2,
        'one': 1,
        'zero': 0,
    }

    tokens: List[str] = input_sequence.split(' ')
    filtered_words: List[str] = [word for word in tokens if word != '']
    temp_sorted: List[str] = filtered_words.copy()

    n: int = len(temp_sorted)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if mapping_dict[temp_sorted[j]] < mapping_dict[temp_sorted[i]]:
                temp_sorted[i], temp_sorted[j] = temp_sorted[j], temp_sorted[i]

    final_string: str = ''
    for k, word in enumerate(temp_sorted):
        if k == 0:
            final_string = word
        else:
            final_string += ' ' + word

    return final_string