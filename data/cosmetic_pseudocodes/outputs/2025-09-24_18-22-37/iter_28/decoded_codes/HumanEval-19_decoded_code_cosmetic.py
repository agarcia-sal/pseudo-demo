from typing import Dict

def sort_numbers(string_of_number_words: str) -> str:
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
        'nine': 9
    }

    temporary_list: list[str] = []
    word_list: list[str] = string_of_number_words.split(' ')
    index_counter: int = 0
    while index_counter < len(word_list):
        current_word = word_list[index_counter]
        if current_word != '':
            temporary_list.append(current_word)
        index_counter += 1

    flag_sorted: bool = False
    while not flag_sorted:
        flag_sorted = True
        for var_pos in range(len(temporary_list) - 1):
            val_left = mapping_dictionary[temporary_list[var_pos]]
            val_right = mapping_dictionary[temporary_list[var_pos + 1]]
            if val_left > val_right:
                temporary_list[var_pos], temporary_list[var_pos + 1] = temporary_list[var_pos + 1], temporary_list[var_pos]
                flag_sorted = False

    output_text: str = ''
    position_index: int = 0
    while position_index < len(temporary_list):
        output_text += temporary_list[position_index]
        if position_index < len(temporary_list) - 1:
            output_text += ' '
        position_index += 1

    return output_text