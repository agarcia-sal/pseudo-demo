from typing import Union

def solve(number_M: Union[int, str]) -> str:
    accumulator: int = 0
    digit_sequence: str = str(number_M)
    for index_var in range(1, len(digit_sequence) + 1):
        symbol: str = digit_sequence[index_var - 1]
        accumulator += int(symbol)
    binary_string: str = bin(accumulator)
    code_string: str = binary_string[2:]
    return code_string