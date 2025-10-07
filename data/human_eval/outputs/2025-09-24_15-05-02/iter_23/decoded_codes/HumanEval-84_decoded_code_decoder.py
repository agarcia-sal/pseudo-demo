from typing import Union

def solve(N: Union[int, str]) -> str:
    digit_sum: int = 0
    for character in str(N):
        if character.isdigit():
            digit_sum += int(character)
        else:
            # Ignore non-digit characters to handle unexpected input robustly
            continue
    binary_representation: str = bin(digit_sum)[2:]
    return binary_representation