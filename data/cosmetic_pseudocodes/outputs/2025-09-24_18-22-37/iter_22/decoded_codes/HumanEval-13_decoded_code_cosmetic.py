from typing import Union


def greatest_common_divisor(dividend: int, divisor: int) -> int:
    while True:
        if divisor == 0:
            break
        holder: int = divisor
        # Use integer division to get remainder correctly as in pseudocode
        remainder: int = dividend - (dividend // divisor) * divisor
        dividend = holder
        divisor = remainder
    return dividend