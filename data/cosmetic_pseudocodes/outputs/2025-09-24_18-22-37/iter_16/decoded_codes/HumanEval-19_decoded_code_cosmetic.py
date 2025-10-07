from typing import Dict, List


def sort_numbers(fragile_string: str) -> str:
    mapping_dictionary: Dict[str, int] = {
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

    words_split: List[str] = fragile_string.split(' ')
    intermediate_array: List[str] = []
    temporary_index: int = 0
    length_words: int = len(words_split)
    while temporary_index < length_words:
        potential_word = words_split[temporary_index]
        if potential_word == '':
            temporary_index += 1
            continue
        intermediate_array.append(potential_word)
        temporary_index += 1

    sorted_array: List[str] = []
    while intermediate_array:
        smallest_word = intermediate_array[0]
        traverse_index = 1
        while traverse_index < len(intermediate_array):
            candidate_word = intermediate_array[traverse_index]
            current_value = mapping_dictionary[smallest_word]
            candidate_value = mapping_dictionary[candidate_word]
            if candidate_value < current_value:
                smallest_word = candidate_word
            traverse_index += 1
        sorted_array.append(smallest_word)
        intermediate_array.remove(smallest_word)

    result_string = ''
    join_index = 0
    while join_index < len(sorted_array):
        current_join = sorted_array[join_index]
        if join_index == len(sorted_array) - 1:
            result_string += current_join
        else:
            result_string += current_join + ' '
        join_index += 1

    return result_string