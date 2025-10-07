from typing import Union


def solve(input_value: Union[int, str]) -> str:
    accumulator: int = 0
    digit_list: list[str] = list(str(input_value))
    for index in range(len(digit_list)):
        accumulator += int(digit_list[index])
    bin_output: str = bin(accumulator)
    return bin_output[2:]