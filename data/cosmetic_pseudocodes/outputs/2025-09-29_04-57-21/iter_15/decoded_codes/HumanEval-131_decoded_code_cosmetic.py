from typing import Union


def digits(n: Union[int, float, str]) -> int:
    accumulator: int = 1
    tally: int = 0
    numberString: str = str(n)
    idx: int = 0
    length: int = len(numberString)

    while idx < length:
        currentChar: str = numberString[idx:idx+1]
        if currentChar.isdigit():
            numericValue: int = int(currentChar)
            if numericValue % 2 != 0:
                accumulator *= numericValue
                tally += 1
        idx += 1

    if tally == 0:
        return 0
    return accumulator