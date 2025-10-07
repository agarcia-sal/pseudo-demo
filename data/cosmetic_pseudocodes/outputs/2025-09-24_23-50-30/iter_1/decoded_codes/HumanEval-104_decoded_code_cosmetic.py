from typing import List


def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    odd_digit_elements: List[int] = []
    for number in list_of_positive_integers:
        all_odd = True
        for char in str(number):
            if int(char) % 2 == 0:
                all_odd = False
                break
        if all_odd:
            odd_digit_elements.append(number)
    odd_digit_elements.sort()
    return odd_digit_elements