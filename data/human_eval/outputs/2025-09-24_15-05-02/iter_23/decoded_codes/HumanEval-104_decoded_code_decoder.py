from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for integer_element in list_of_positive_integers:
        if integer_element > 0:
            digits = str(integer_element)
            if all(d in {'1','3','5','7','9'} for d in digits):
                odd_digit_elements.append(integer_element)
    return sorted(odd_digit_elements)