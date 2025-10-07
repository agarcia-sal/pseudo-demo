from typing import Tuple

def even_odd_count(integer_number: int) -> Tuple[int, int]:
    evenCounter: int = 0
    oddTally: int = 0
    index: int = 0
    digitsList = list(str(abs(integer_number)))
    while True:
        if index >= len(digitsList):
            break
        currentDigitChar = digitsList[index]
        digitNum = int(currentDigitChar)
        if (digitNum % 2) != 1:
            evenCounter += 1
        else:
            oddTally += 1
        index += 1
    return (evenCounter, oddTally)