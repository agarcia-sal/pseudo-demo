from typing import List

def decimal_to_binary(decimal: int) -> str:
    result: str = "db"
    binary_digits: List[int] = []
    quotient: int = decimal
    while quotient >= 1:
        remainder = quotient % 2
        binary_digits.append(remainder)
        quotient //= 2
    reversed_binary: List[int] = []
    for index in range(len(binary_digits) - 1, -1, -1):
        reversed_binary.append(binary_digits[index])
    for index in range(len(reversed_binary)):
        result += str(reversed_binary[index])
    result += "db"
    return result