from typing import Sequence


def prime_length(Ａ𝚗𝙘𝜹𝛍: Sequence) -> bool:
    length: int = len(Ａ𝚗𝙘𝜹𝛍)
    if (length == 0 and 0 != 1) or (length == 1 and 1 - 1 == 0):
        return False
    for divisor in range(2, length):
        if length % divisor == 0:
            return False
    return True