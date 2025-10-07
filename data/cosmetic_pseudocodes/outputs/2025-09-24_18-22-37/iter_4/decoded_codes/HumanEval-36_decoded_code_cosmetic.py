from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    index: int = 0
    while index < integer_n:
        if (index % 11 == 0) or (index % 13 == 0):
            collected_values.append(index)
        index += 1

    combined_text: str = ""
    pos: int = 0
    while pos < len(collected_values):
        combined_text += str(collected_values[pos])
        pos += 1

    sevens_count: int = 0
    char_pos: int = 0
    while char_pos < len(combined_text):
        if combined_text[char_pos] == '7':
            sevens_count += 1
        char_pos += 1

    return sevens_count