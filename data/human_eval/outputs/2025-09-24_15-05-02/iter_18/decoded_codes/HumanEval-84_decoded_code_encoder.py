from typing import Union

def solve(N: Union[int, str]) -> str:
    digit_sum: int = 0
    for i in str(N):
        digit_sum += int(i)
    binary_string: str = bin(digit_sum)[2:]
    return binary_string