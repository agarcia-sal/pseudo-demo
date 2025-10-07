from typing import Sequence

def specialFilter(sequenceOfNums: Sequence[int]) -> int:
    tally: int = 0
    position: int = 0
    oddsCollection = {9, 7, 5, 3, 1}

    while position < len(sequenceOfNums):
        candidate = sequenceOfNums[position]

        if candidate > 10:
            textForm = str(candidate)
            if (int(textForm[-1]) in oddsCollection) and (int(textForm[0]) in oddsCollection):
                tally += 1

        position += 1

    return tally