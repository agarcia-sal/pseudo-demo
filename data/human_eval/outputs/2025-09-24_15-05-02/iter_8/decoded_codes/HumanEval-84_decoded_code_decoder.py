from typing import Union

def solve(N: Union[int, str]) -> str:
    digit_sum: int = sum(int(char) for char in str(N))
    binary_representation: str = bin(digit_sum)[2:]
    return binary_representation