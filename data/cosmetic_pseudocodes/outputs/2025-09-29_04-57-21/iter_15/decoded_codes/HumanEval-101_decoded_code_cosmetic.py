from typing import List

def words_string(input_string: str) -> List[str]:
    if input_string == "":
        return []

    buffer: List[str] = []

    index: int = 0
    while index < len(input_string):
        current_char: str = input_string[index]

        if current_char == ',':
            buffer.append(' ')
        else:
            buffer.append(current_char)

        index += 1

    rebuilt_string: str = ""
    for element in buffer:
        rebuilt_string += element

    return rebuilt_string.split()