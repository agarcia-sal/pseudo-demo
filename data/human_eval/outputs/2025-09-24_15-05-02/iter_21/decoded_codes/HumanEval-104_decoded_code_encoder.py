from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for integer_element in list_of_positive_integers:
        # Check if all digits are odd
        if all((int(digit) % 2 == 1) for digit in str(integer_element)):
            odd_digit_elements.append(integer_element)
    sorted_list = sorted(odd_digit_elements)
    return sorted_list