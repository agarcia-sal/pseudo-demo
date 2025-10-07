from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    current_index: int = 0
    while current_index < integer_n:
        if not (current_index % 11 != 0 and current_index % 13 != 0):
            collected_values.append(current_index)
        current_index += 1

    merged_text: str = ""
    idx: int = 0
    while idx < len(collected_values):
        merged_text += str(collected_values[idx])
        idx += 1

    seven_counter: int = 0
    position: int = 0
    while position < len(merged_text):
        if merged_text[position] == '7':
            seven_counter += 1
        position += 1

    return seven_counter