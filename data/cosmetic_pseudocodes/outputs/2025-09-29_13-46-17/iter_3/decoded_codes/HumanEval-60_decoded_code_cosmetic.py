def sum_to_n(numberLimit: int) -> int:
    accumulator: int = 0
    currentIndex: int = 0

    while currentIndex <= numberLimit:
        accumulator += currentIndex
        currentIndex += 1

    return accumulator