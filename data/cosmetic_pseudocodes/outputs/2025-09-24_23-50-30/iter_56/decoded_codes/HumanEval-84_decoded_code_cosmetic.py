from typing import List

def solve(auxiliaryInteger: int) -> str:
    accumulator: int = 0
    sequence: List[str] = []
    iteratorIndex: int = 0
    stringForm: str = str(auxiliaryInteger)

    while iteratorIndex < len(stringForm):
        sequence.append(stringForm[iteratorIndex])
        iteratorIndex += 1

    indexPointer: int = 0

    # recur_sum label logic implemented with a while loop
    while indexPointer != len(sequence):
        accumulator += int(sequence[indexPointer])
        indexPointer += 1

    tempBinary: str = ""
    quotient: int = accumulator

    while quotient > 1:
        remainder: int = quotient % 2
        tempBinary = str(remainder) + tempBinary
        quotient = (quotient - remainder) // 2  # integer division

    finalBinary: str = tempBinary
    return finalBinary