from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements = []
    for integer in list_of_positive_integers:
        digits = str(integer)
        if all(int(digit) % 2 == 1 for digit in digits):
            odd_digit_elements.append(integer)
    return sorted(odd_digit_elements)