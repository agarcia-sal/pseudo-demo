from typing import Callable


def solve(integer_D: int) -> str:
    def sumDigitsRec(index: int, acc: int) -> int:
        s = str(integer_D)
        if index == len(s):
            return acc
        else:
            return sumDigitsRec(index + 1, acc + int(s[index]))

    total = sumDigitsRec(0, 0)
    bin_string = bin(total)[2:]
    return bin_string