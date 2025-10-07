from typing import List


def words_string(input_string: str) -> List[str]:
    input_length: int = len(input_string)
    if input_length == 0:
        return []
    modified_chars: List[str] = [''] * input_length
    index_counter: int = 0
    while index_counter < input_length:
        current_char: str = input_string[index_counter]
        if current_char != ',':
            modified_chars[index_counter] = current_char
            index_counter += 1
            continue
        modified_chars[index_counter] = ' '
        index_counter += 1
    accumulated_string: str = ''
    concatenate_index: int = 0
    modified_length: int = len(modified_chars)
    while concatenate_index < modified_length:
        accumulated_string += modified_chars[concatenate_index]
        concatenate_index += 1
    resulting_words: List[str] = accumulated_string.split()
    return resulting_words