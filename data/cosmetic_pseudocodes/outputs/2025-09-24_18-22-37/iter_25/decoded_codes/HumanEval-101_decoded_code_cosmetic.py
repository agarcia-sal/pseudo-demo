from typing import List


def words_string(input_string: str) -> List[str]:
    temp_buffer: List[str] = []

    if input_string != "":
        index_var: int = 0
        length_limit: int = len(input_string)

        while index_var < length_limit:
            current_char: str = input_string[index_var]

            if current_char != ",":
                temp_char: str = current_char
            else:
                temp_char = " "

            temp_buffer.append(temp_char)
            index_var += 1

        assembled_string: str = ""
        pos_tracker: int = 0
        total_chars: int = len(temp_buffer)

        while pos_tracker < total_chars:
            assembled_string += temp_buffer[pos_tracker]
            pos_tracker += 1

        result_list: List[str] = []
        accumulated_word: str = ""
        char_pos: int = 0
        string_length: int = len(assembled_string)

        while char_pos < string_length:
            current_char = assembled_string[char_pos]

            if current_char != " " and current_char != "\t" and current_char != "\n":
                accumulated_word += current_char
            else:
                if accumulated_word != "":
                    result_list.append(accumulated_word)
                    accumulated_word = ""
            char_pos += 1

        if accumulated_word != "":
            result_list.append(accumulated_word)

        return result_list
    else:
        return []