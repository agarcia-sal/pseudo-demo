from typing import List


def fizz_buzz(integer_n: int) -> int:
    collected_values: List[int] = []
    current_index: int = 0
    while current_index < integer_n:
        # Append current_index only if it is divisible by 11 or by 13 (the negation of the given condition)
        if not (current_index % 11 != 0 and current_index % 13 != 0):
            collected_values.append(current_index)
        current_index += 1

    merged_text: str = ""
    temp_iter: int = 0
    while temp_iter < len(collected_values):
        merged_text += str(collected_values[temp_iter])
        temp_iter += 1

    seven_count: int = 0
    pos: int = 0
    while pos < len(merged_text):
        if merged_text[pos] == '7':
            seven_count += 1
        pos += 1

    return seven_count