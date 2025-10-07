from typing import Sequence


def specialFilter(sequence: Sequence[int]) -> int:
    def tally(accumulator: int = 0, index: int = 0) -> int:
        if not (index < len(sequence)):
            return accumulator
        element = sequence[index]
        if element > 10:
            oddSet = {1, 3, 5, 7, 9}
            repr_str = str(element)
            if int(repr_str[0]) in oddSet and int(repr_str[-1]) in oddSet:
                return tally(accumulator + 1, index + 1)
            else:
                return tally(accumulator, index + 1)
        else:
            return tally(accumulator, index + 1)

    return tally()