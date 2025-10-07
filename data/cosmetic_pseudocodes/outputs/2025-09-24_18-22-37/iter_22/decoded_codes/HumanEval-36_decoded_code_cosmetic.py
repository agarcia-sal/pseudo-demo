from typing import List


def fizz_buzz(input_limit: int) -> int:
    gathered_values: List[int] = []
    index_j: int = 0
    while index_j < input_limit:
        cond_a: bool = (index_j % 11 == 0)
        cond_b: bool = (index_j % 13 == 0)
        if not (cond_a is False and cond_b is False):
            gathered_values.append(index_j)
        index_j += 1

    merged_text: str = ""
    iter_k: int = 0
    while iter_k < len(gathered_values):
        current_val: int = gathered_values[iter_k]
        merged_text += str(current_val)
        iter_k += 1

    seven_count: int = 0
    pos_m: int = 0
    while pos_m < len(merged_text):
        current_char: str = merged_text[pos_m]
        if current_char == '7':
            seven_count += 1
        pos_m += 1

    return seven_count