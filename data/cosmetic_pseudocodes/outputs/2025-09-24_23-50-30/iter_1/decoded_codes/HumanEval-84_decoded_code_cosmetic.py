from typing import List


def solve(integer_N: int) -> str:
    digitSum: int = 0
    digitsArray: List[str] = list(str(integer_N))
    i: int = 0

    while i < len(digitsArray):
        digitSum += int(digitsArray[i])
        i += 1

    binaryStr: str = bin(digitSum)
    result: str = binaryStr[3:]  # remove '0b' prefix and the next character
    return result