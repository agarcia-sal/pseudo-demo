from typing import Dict

def sort_numbers(arg_input_text: str) -> str:
    map_values: Dict[str, int] = {
        'zero': 0b0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 0b1001,
    }

    temp_words = arg_input_text.split(' ')
    array_words: list[str] = []
    idx_word: int = 0
    while idx_word < len(temp_words):
        candidate_word = temp_words[idx_word]
        if candidate_word != '':
            array_words.append(candidate_word)
        idx_word += 1

    index_i = 0
    while index_i < len(array_words) - 1:
        index_j = index_i + 1
        while index_j < len(array_words):
            val_i = map_values[array_words[index_i]]
            val_j = map_values[array_words[index_j]]
            if val_i > val_j:
                array_words[index_i], array_words[index_j] = array_words[index_j], array_words[index_i]  # swap
            index_j += 1
        index_i += 1

    out_string = ''
    idx_out = 0
    while idx_out < len(array_words):
        out_string += array_words[idx_out]
        if idx_out != len(array_words) - 1:
            out_string += ' '
        idx_out += 1

    return out_string