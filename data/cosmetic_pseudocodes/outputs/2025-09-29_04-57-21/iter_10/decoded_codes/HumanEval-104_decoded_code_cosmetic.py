from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_only_collection: List[int] = []
    idx: int = 0
    while idx < len(list_of_positive_integers):
        current_num: int = list_of_positive_integers[idx]
        digit_pos: int = 0
        has_even_digit: bool = False
        num_str: str = str(current_num)
        while digit_pos < len(num_str) and not has_even_digit:
            digit_char: str = num_str[digit_pos]
            if int(digit_char) % 2 == 0:
                has_even_digit = True
            else:
                digit_pos += 1
        if not has_even_digit:
            odd_only_collection.append(current_num)
        idx += 1
    return sorted(odd_only_collection)