from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def all_digits_odd(number: int) -> bool:
        while number > 0:
            digit = number % 10
            if digit % 2 == 0:
                return False
            number //= 10
        return True

    odd_digit_elements: List[int] = [
        element for element in list_of_positive_integers if all_digits_odd(element)
    ]
    return sorted(odd_digit_elements)