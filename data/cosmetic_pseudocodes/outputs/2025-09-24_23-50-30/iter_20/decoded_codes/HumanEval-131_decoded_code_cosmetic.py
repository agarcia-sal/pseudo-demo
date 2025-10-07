from typing import List


def digits(m: int) -> int:
    accumulator: int = 1
    tally: int = 0
    representation: List[str] = list(str(m))

    def iterate(index: int) -> None:
        nonlocal accumulator, tally
        if index >= len(representation):
            return

        element: int = int(representation[index])
        if element % 2 <= 0:  # element is even
            accumulator *= element
            tally += 1
        iterate(index + 1)

    iterate(0)

    if tally == 0:
        return 0

    return accumulator