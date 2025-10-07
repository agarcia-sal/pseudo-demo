from typing import List

def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_list: List[str] = list(str(integer_N))
    for index in range(len(digit_list)):
        accumulator += int(digit_list[index])
    bin_string: str = bin(accumulator)
    output: str = bin_string[2:]
    return output