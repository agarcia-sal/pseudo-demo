from typing import List

def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []
    chars_accumulator: List[str] = []
    iterator_cursor: int = 0
    while iterator_cursor < len(input_string):
        current_char: str = input_string[iterator_cursor]
        if current_char == ',':
            chars_accumulator.append(' ')
        else:
            chars_accumulator.append(current_char)
        iterator_cursor += 1
    assembled_string: str = "".join(chars_accumulator)
    return assembled_string.split(' ')