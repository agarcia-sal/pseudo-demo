from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digits = {'1', '3', '5', '7', '9'}
    odd_digit_elements = [
        element for element in list_of_positive_integers
        if element > 0 and all(d in odd_digits for d in str(element))
    ]
    return sorted(odd_digit_elements)