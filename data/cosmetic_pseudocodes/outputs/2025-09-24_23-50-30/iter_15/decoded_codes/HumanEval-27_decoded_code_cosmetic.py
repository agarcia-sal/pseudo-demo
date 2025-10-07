from typing import List

def flip_case(some_text: str) -> str:
    altered_text: List[str] = []
    index_counter: int = 0
    while index_counter < len(some_text):
        current_char: str = some_text[index_counter]
        if current_char == current_char.lower():
            altered_text.append(current_char.upper())
        else:
            altered_text.append(current_char.lower())
        index_counter += 1
    result_string: str = ''.join(altered_text)
    return result_string