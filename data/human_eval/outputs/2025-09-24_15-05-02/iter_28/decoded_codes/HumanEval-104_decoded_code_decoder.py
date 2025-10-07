from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for integer_element in list_of_positive_integers:
        if all((int(c) % 2) == 1 for c in str(integer_element)):
            odd_digit_elements.append(integer_element)
    return sorted(odd_digit_elements)