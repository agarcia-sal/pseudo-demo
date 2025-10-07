from typing import Set


def fizz_buzz(limit: int) -> int:
    sequence: Set[int] = set()
    index: int = 0

    while index < limit:
        # Add index if it is divisible by 11 or 13 (negation of both not divisible)
        if not (index % 11 != 0 and index % 13 != 0):
            sequence.add(index)
        index += 1

    combined: str = "".join(str(element) for element in sequence)

    pointer: int = 0
    count: int = 0

    while pointer < len(combined):
        if combined[pointer] == '7':
            count += 1
        pointer += 1

    return count