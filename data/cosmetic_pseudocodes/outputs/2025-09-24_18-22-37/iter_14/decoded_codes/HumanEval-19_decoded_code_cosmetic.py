from typing import List

def sort_numbers(alpha_sequence: str) -> str:
    digit_values: dict[str, int] = {
        'one': 0x1,
        'two': 0x2,
        'seven': 0x7,
        'four': 0x4,
        'eight': 0x8,
        'five': 0x5,
        'three': 0x3,
        'six': 0x6,
        'zero': 0x0,
        'nine': 0x9,
    }

    temp_list: List[str] = []
    split_words: List[str] = alpha_sequence.split(" ")

    index_var: int = 0
    while index_var < len(split_words):
        current_string: str = split_words[index_var]
        if current_string != "":
            temp_list.append(current_string)
        index_var += 1

    sorted_words: List[str] = temp_list[:]

    loop_var: int = 1
    while loop_var < len(sorted_words):
        key_word: str = sorted_words[loop_var]
        inner_var: int = loop_var - 1

        # Insertion sort based on digit_values
        while inner_var >= 0 and digit_values[key_word] < digit_values[sorted_words[inner_var]]:
            sorted_words[inner_var + 1] = sorted_words[inner_var]
            inner_var -= 1

        sorted_words[inner_var + 1] = key_word
        loop_var += 1

    result_string: str = ""
    concat_index: int = 0

    while concat_index < len(sorted_words):
        current_word: str = sorted_words[concat_index]
        if concat_index == 0:
            result_string = current_word
        else:
            result_string = result_string + " " + current_word
        concat_index += 1

    return result_string