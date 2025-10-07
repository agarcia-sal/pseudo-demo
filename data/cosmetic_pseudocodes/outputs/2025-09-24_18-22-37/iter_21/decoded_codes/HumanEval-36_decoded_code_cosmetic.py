from typing import List

def fizz_buzz(param_x: int) -> int:
    collection_a: List[int] = []
    idx_b: int = 0
    while True:
        if idx_b >= param_x:
            break
        div_by_11: bool = (idx_b % 11) == 0
        div_by_13: bool = (idx_b % 13) == 0

        # Append idx_b if divisible by 11 or 13
        if div_by_11 or div_by_13:
            collection_a.append(idx_b)

        idx_b += 1

    combined_str: str = "".join(str(element_c) for element_c in collection_a)

    counter_d: int = 0
    pos_e: int = 1
    while pos_e <= len(combined_str):
        current_char_f: str = combined_str[pos_e - 1]
        if current_char_f == '7':
            counter_d += 1
        pos_e += 1

    return counter_d