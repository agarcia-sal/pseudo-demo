from typing import List

def change_base(integer_x: int, integer_base: int) -> str:
    list_digits: List[str] = []

    def accumulate_digits(number: int) -> None:
        if number == 0:
            return
        accumulate_digits(number // integer_base)
        remainder_digit = number % integer_base
        list_digits.append(str(remainder_digit))

    if integer_x == 0:
        return ""
    accumulate_digits(integer_x)
    return ''.join(list_digits)