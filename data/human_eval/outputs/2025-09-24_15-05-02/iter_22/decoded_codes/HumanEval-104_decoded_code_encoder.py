from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for integer_value in list_of_positive_integers:
        has_only_odd_digits = True
        for digit_character in str(integer_value):
            digit_value = int(digit_character)
            if digit_value % 2 == 0:
                has_only_odd_digits = False
                break
        if has_only_odd_digits:
            odd_digit_elements.append(integer_value)
    return sorted(odd_digit_elements)