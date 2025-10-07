from typing import List

def unique_digits(list_of_positive_integers: List[int]) -> List[int]:
    def digits_odd(n: int) -> bool:
        if n == 0:
            return True
        current_digit = n % 10
        if current_digit % 2 == 0:
            return False
        return digits_odd(n // 10)

    odd_only_numbers: List[int] = []
    for current_number in list_of_positive_integers:
        if digits_odd(current_number):
            odd_only_numbers.append(current_number)

    odd_only_numbers.sort()
    return odd_only_numbers