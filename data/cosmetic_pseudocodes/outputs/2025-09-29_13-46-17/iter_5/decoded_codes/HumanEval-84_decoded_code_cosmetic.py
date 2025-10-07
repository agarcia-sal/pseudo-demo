from typing import Tuple


def solve(integer_N: int) -> str:
    def accumulateDigits(digitsStr: str, idx: int, total: int) -> int:
        if idx >= len(digitsStr):
            return total
        return accumulateDigits(digitsStr, idx + 1, total + (ord(digitsStr[idx]) - ord('0')))

    digitStrRepr: str = str(integer_N)
    accumulatedSum_in_snake_case: int = accumulateDigits(digitStrRepr, 0, 0)
    binary_str: str = bin(accumulatedSum_in_snake_case)
    # Extract substring from index 2 to end (inclusive)
    # Note: In Python slicing, end is exclusive, so the slice is [2:len(binary_str)]
    binary_form_final: str = binary_str[2:len(binary_str)]
    return binary_form_final