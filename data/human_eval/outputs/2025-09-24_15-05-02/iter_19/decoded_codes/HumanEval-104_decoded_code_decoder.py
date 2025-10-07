from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for number in list_of_positive_integers:
        if all(int(digit) % 2 == 1 for digit in str(number)):
            odd_digit_elements.append(number)
    return sorted(odd_digit_elements)