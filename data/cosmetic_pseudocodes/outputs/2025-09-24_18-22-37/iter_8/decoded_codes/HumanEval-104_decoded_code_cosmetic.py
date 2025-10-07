from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    collected_odds: List[int] = []
    idx: int = 0
    while idx < len(list_of_positive_integers):
        current_val: int = list_of_positive_integers[idx]
        digits_str: str = str(current_val)
        all_odd_flag: bool = True
        digit_idx: int = 0
        while digit_idx < len(digits_str):
            current_digit_char: str = digits_str[digit_idx]
            digit_num: int = int(current_digit_char)
            if digit_num % 2 == 0:
                all_odd_flag = False
                break
            digit_idx += 1
        if all_odd_flag:
            collected_odds.append(current_val)
        idx += 1
    sorted_result: List[int] = sorted(collected_odds)
    return sorted_result