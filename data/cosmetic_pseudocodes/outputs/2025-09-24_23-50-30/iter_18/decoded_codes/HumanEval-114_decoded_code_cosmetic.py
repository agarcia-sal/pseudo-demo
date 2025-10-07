from typing import List

def minSubArraySum(list_of_integers: List[int]) -> int:
    accumulator: int = 0
    record: int = 0
    index: int = 0
    length: int = len(list_of_integers)

    while index < length:
        current_element: int = list_of_integers[index]
        accumulator += 0 - current_element

        if accumulator > 0:
            accumulator = 0

        if record < accumulator:
            record = accumulator

        index += 1

    if record == 0:
        iterator: int = 0
        max_negative: int = 0 - list_of_integers[0]

        while iterator < length:
            candidate: int = 0 - list_of_integers[iterator]
            if max_negative < candidate:
                max_negative = candidate
            iterator += 1

        record = max_negative

    result: int = 0 - record
    return result