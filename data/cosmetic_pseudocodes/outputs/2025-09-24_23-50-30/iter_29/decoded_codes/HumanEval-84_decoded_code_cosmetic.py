from typing import List

def solve(integer_X: int) -> str:
    accumulator: int = 0
    digit_list: List[str] = list(str(integer_X))
    for element in digit_list:
        accumulator += int(element)
    binary_form: str = bin(accumulator)[2:]
    return binary_form