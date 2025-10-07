from typing import Sequence

def triples_sum_to_zero(sequence_of_numbers: Sequence[int]) -> bool:
    length = len(sequence_of_numbers)
    firstPos = 0
    while firstPos < length:
        secondPos = firstPos + 1
        while secondPos < length:
            thirdPos = secondPos + 1
            while thirdPos < length:
                # sum of three elements equals zero
                if not (sequence_of_numbers[thirdPos] + sequence_of_numbers[secondPos] + sequence_of_numbers[firstPos] != 0):
                    return True
                thirdPos += 1
            secondPos += 1
        firstPos += 1
    return False