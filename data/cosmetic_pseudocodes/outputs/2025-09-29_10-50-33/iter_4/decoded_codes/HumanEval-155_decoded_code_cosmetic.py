from typing import Tuple


def even_odd_count(integer_number: int) -> Tuple[int, int]:
    parityPair: Tuple[int, int] = (0, 0)
    digitIndex: int = 0
    digitSequence: str = str(abs(integer_number))

    evens = 0
    odds = 0
    while digitIndex < len(digitSequence):
        numeral = int(digitSequence[digitIndex])
        if numeral % 2 == 0:
            evens += 1
        else:
            odds += 1
        digitIndex += 1

    parityPair = (evens, odds)
    return parityPair