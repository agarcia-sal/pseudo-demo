from typing import List


def words_string(input_string: str) -> List[str]:
    if len(input_string) == 0:
        return []

    temp_chars: List[str] = []
    for index in range(len(input_string)):
        current_char = input_string[index]
        if current_char == ',':
            temp_chars.append(' ')
        else:
            temp_chars.append(current_char)

    merged_string = "".join(temp_chars)
    return merged_string.split()