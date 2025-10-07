from typing import Union

def solve(N: Union[int, str]) -> str:
    digit_sum = 0
    for digit_char in str(N):
        if not digit_char.isdigit():
            raise ValueError("Input contains non-digit characters")
        digit_sum += int(digit_char)
    binary_representation = bin(digit_sum)[2:]
    return binary_representation