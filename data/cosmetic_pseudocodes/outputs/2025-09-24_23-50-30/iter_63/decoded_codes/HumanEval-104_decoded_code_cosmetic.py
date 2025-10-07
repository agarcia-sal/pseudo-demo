from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    index: int = 0
    while index < len(list_of_positive_integers):
        current_num: int = list_of_positive_integers[index]
        is_all_odd: bool = True
        digits_str: str = str(current_num)
        pos: int = 0
        while pos < len(digits_str) and is_all_odd:
            digit_char: str = digits_str[pos]
            digit_val: int = ord(digit_char) - ord('0')
            is_all_odd = not (digit_val % 2 == 0)
            pos += 1
        if is_all_odd:
            odd_digit_elements.append(current_num)
        index += 1
    return sorted(odd_digit_elements)