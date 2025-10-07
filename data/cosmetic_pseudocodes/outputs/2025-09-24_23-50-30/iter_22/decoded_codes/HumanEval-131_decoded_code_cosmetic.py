from typing import List


def digits(x: int) -> int:
    accumulator: int = 1
    tally: int = 0
    array_of_chars: List[str] = [ch for ch in str(x)]

    def process_items(items: List[str], pos: int) -> None:
        nonlocal accumulator, tally
        if pos >= len(items):
            return
        current = int(items[pos])
        if current % 2 == 1:
            accumulator *= current
            tally += 1
        process_items(items, pos + 1)

    process_items(array_of_chars, 0)
    return 0 if tally == 0 else accumulator