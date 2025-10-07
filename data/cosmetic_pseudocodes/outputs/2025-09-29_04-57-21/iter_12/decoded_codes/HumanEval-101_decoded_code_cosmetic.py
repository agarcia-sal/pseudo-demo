from typing import List


def words_string(input_string: str) -> List[str]:
    if input_string != "":
        intermediate_chars: List[str] = []
        index_tracker: int = 0

        while index_tracker < len(input_string):
            current_char: str = input_string[index_tracker]

            if not (current_char != ','):
                intermediate_chars.append(' ')
            else:
                intermediate_chars.append(current_char)

            index_tracker += 1

        assembled_string: str = ""
        pos: int = 0

        while pos < len(intermediate_chars):
            assembled_string += intermediate_chars[pos]
            pos += 1

        return assembled_string.split()

    return []