from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements = []
    for element in list_of_positive_integers:
        if all(int(digit) % 2 == 1 for digit in str(element)):
            odd_digit_elements.append(element)
    sorted_result = sorted(odd_digit_elements)
    return sorted_result