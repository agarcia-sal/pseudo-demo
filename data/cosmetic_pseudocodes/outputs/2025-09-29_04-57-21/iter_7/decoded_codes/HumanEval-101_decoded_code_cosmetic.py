from typing import List

def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []

    buffer: List[str] = []
    idx: int = 0
    while idx < len(input_string):
        current_char = input_string[idx]
        if current_char == ',':
            buffer.append(' ')
        else:
            buffer.append(current_char)
        idx += 1

    assembled = ""
    for element in buffer:
        assembled += element

    return assembled.split()