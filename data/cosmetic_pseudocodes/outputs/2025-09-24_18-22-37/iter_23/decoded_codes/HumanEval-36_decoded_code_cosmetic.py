from typing import List


def fizz_buzz(integer_n: int) -> int:
    gathered_values: List[int] = []
    idx: int = 0
    while idx < integer_n:
        cond_one = idx % 11
        cond_two = idx % 13
        if cond_one == 0 or cond_two == 0:
            gathered_values.append(idx)
        idx += 1

    assembled_str: str = ""
    position: int = 0
    while position < len(gathered_values):
        val_element = gathered_values[position]
        assembled_str += str(val_element)
        position += 1

    seven_counter: int = 0
    letter_idx: int = 0
    while letter_idx < len(assembled_str):
        curr_char = assembled_str[letter_idx]
        if curr_char == '7':
            seven_counter += 1
        letter_idx += 1

    return seven_counter