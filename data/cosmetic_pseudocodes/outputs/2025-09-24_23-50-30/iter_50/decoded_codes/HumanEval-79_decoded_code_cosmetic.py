from typing import List


def decimal_to_binary(value: int) -> str:
    pieces: List[str] = ["db"]
    digits: List[int] = []
    n: int = value
    while n > 1:
        remainder = n % 2
        digits.append(remainder)
        n = (n - remainder) // 2
    digits.append(1)
    binary_string = "".join(str(digits[i]) for i in range(len(digits) - 1, -1, -1))
    pieces.append(binary_string)
    pieces.append("db")
    return "".join(pieces)