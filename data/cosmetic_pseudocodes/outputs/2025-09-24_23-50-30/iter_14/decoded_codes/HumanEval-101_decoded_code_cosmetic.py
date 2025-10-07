from typing import List

def words_string(input_string: str) -> List[str]:
    if not input_string:
        return []
    modified_chars: List[str] = []
    index: int = 0
    while index < len(input_string):
        current_char: str = input_string[index]
        if current_char == ',':
            modified_chars.append(' ')
        else:
            modified_chars.append(current_char)
        index += 1
    result_string: str = ''.join(modified_chars)
    return result_string.split()