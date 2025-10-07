from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for number in list_of_positive_integers:
        digits_are_all_odd = True
        for digit_char in str(number):
            if int(digit_char) % 2 == 0:
                digits_are_all_odd = False
                break
        if digits_are_all_odd:
            odd_digit_elements.append(number)
    odd_digit_elements.sort()
    return odd_digit_elements