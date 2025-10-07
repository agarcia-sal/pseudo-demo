from typing import Dict

def sort_numbers(numeral_sequence: str) -> str:
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

    temp_words = numeral_sequence.split(' ')
    words_list = [word for word in temp_words if word != '']

    # Bubble sort on words_list using digit_values for comparison
    while True:
        changed = False
        pos = 1
        while pos < len(words_list):
            first_val = digit_values[words_list[pos - 1]]
            second_val = digit_values[words_list[pos]]
            if first_val > second_val:
                words_list[pos - 1], words_list[pos] = words_list[pos], words_list[pos - 1]
                changed = True
            pos += 1
        if not changed:
            break

    joined_result = ''
    pointer = 0
    while pointer < len(words_list):
        joined_result += words_list[pointer]
        if pointer < len(words_list) - 1:
            joined_result += ' '
        pointer += 1

    return joined_result