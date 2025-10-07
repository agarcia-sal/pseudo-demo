from typing import Union

def greatest_common_divisor(first_number: int, second_number: int) -> int:
    while second_number != 0:
        temp_holder: int = second_number
        second_number = first_number - (first_number // second_number) * second_number
        first_number = temp_holder
    return first_number