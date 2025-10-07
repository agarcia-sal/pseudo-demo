from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for integer_element in range(len(list_of_positive_integers)):
        current_number = list_of_positive_integers[integer_element]
        digits_are_odd = True
        while current_number > 0 and digits_are_odd:
            digit = current_number % 10
            if digit % 2 == 0:
                digits_are_odd = False
            current_number //= 10
        if digits_are_odd:
            odd_digit_elements.append(list_of_positive_integers[integer_element])
    odd_digit_elements.sort()
    return odd_digit_elements