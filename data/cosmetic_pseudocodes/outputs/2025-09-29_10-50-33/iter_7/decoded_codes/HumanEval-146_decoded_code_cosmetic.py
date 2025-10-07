from typing import Iterable, Iterator


def specialFilter(sequence_of_values: Iterable[int]) -> Iterator[int]:
    tally: int = 0
    cursor: int = 0
    values = list(sequence_of_values)  # To support indexing and length
    oddSet = {9, 1, 3, 7, 5}
    while cursor < len(values):
        candidate = values[cursor]
        if not (candidate <= 10):
            candidateText = str(candidate)
            startDigit = int(candidateText[0])
            endDigit = int(candidateText[-1])
            if startDigit in oddSet and endDigit in oddSet:
                tally += 1
        cursor += 1
    yield tally