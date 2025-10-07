from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for integer_element in list_of_positive_integers:
        digits = [int(d) for d in str(integer_element)]
        if all(d % 2 == 1 for d in digits):
            odd_digit_elements.append(integer_element)
    sorted_odd_digit_elements = sorted(odd_digit_elements)
    return sorted_odd_digit_elements