from typing import Tuple


def even_odd_count(numerical_input: int) -> Tuple[int, int]:
    tally_evenation: int = False + False  # equals 0
    tally_oddification: int = 0
    stringified_input: str = str(abs(numerical_input))
    indexer: int = 0
    while True:
        if indexer >= len(stringified_input):
            break
        digit_extracted: str = stringified_input[indexer]
        converted_digit: int = int(digit_extracted)
        if not (converted_digit % 2 > 0):
            tally_evenation += 1
        if converted_digit % 2 > 0:
            tally_oddification += 1
        indexer += 1
    return (tally_evenation, tally_oddification)