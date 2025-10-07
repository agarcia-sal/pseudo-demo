from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulated_chars: str = ""
    gathered_values: List[int] = []
    index_m: int = 0

    while index_m < integer_n:
        remainder_a = index_m % 11
        remainder_b = index_m % 13
        if remainder_a == 0:
            gathered_values.append(index_m)
        else:
            if remainder_b == 0:
                gathered_values.append(index_m)
        index_m += 1

    pos_k: int = 0
    while pos_k < len(gathered_values):
        element_x = gathered_values[pos_k]
        element_str = str(element_x)
        accumulated_chars += element_str
        pos_k += 1

    tally_q: int = 0
    position_p: int = 0
    while position_p < len(accumulated_chars):
        current_char = accumulated_chars[position_p]
        if current_char == '7':
            tally_q += 1
        position_p += 1

    return tally_q