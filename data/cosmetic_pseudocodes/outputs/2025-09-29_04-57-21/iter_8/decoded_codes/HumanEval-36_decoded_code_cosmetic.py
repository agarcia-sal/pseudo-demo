from typing import List

def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    current_index: int = 0
    while current_index < integer_n:
        if not (current_index % 11 != 0 and current_index % 13 != 0):
            collected_values.append(current_index)
        current_index += 1

    merged_text: str = ""
    iterator: int = 0
    while iterator < len(collected_values):
        merged_text += str(collected_values[iterator])
        iterator += 1

    seven_char_count: int = 0
    text_pos: int = 0
    while text_pos < len(merged_text):
        if merged_text[text_pos] == '7':
            seven_char_count += 1
        text_pos += 1

    return seven_char_count