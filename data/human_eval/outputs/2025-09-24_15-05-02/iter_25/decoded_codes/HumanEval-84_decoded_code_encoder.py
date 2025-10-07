from typing import Union

def solve(N: Union[int, str]) -> str:
    digits = str(N)
    if len(digits) <= 1:
        # sum of digits in an empty or single-digit number excluding last digit is 0
        digit_sum = 0
    else:
        digit_sum = sum(int(char) for char in digits[:-1])
    return bin(digit_sum)[2:]