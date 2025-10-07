from typing import Optional


def solve(integer_N: int) -> str:
    def digitSumRec(chars: str, accumulator: int) -> int:
        if chars == "":
            return accumulator
        currentChar = chars[0]
        restChars = chars[1:]
        return digitSumRec(restChars, accumulator + int(currentChar))

    stringInput: str = str(integer_N)
    total: int = digitSumRec(stringInput, 0)
    trimmedBinary: str = bin(total)[2:]
    return trimmedBinary