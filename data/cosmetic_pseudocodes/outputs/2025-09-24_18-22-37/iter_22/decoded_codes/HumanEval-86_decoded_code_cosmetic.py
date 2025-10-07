from typing import List


def anti_shuffle(text_parameter: str) -> str:
    tokens: List[str] = []
    temp_str: str = text_parameter

    while " " in temp_str:
        idx_space: int = temp_str.index(" ")
        current_token: str = temp_str[:idx_space]
        tokens.append(current_token)
        temp_str = temp_str[idx_space + 1:]
    tokens.append(temp_str)

    accumulating_list: List[str] = []
    iterator_index: int = 0

    while iterator_index < len(tokens):
        current_token: str = tokens[iterator_index]
        char_array: List[str] = []

        char_pos: int = 0
        while char_pos < len(current_token):
            char_array.append(current_token[char_pos])
            char_pos += 1

        needing_sort: bool = True
        while needing_sort:
            needing_sort = False
            j: int = 0
            while j < len(char_array) - 1:
                if not (char_array[j] <= char_array[j + 1]):
                    char_array[j], char_array[j + 1] = char_array[j + 1], char_array[j]
                    needing_sort = True
                j += 1

        rebuilt_word_chars: str = ""
        k: int = 0
        while k < len(char_array):
            rebuilt_word_chars += char_array[k]
            k += 1

        accumulating_list.append(rebuilt_word_chars)
        iterator_index += 1

    output_str: str = ""
    idx_output: int = 0
    while idx_output < len(accumulating_list):
        output_str += accumulating_list[idx_output]
        if idx_output < len(accumulating_list) - 1:
            output_str += " "
        idx_output += 1

    return output_str