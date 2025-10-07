from typing import Callable


def solve(inputVal: int) -> str:
    def digitAccumulator(index: int, total: int) -> int:
        if index == len(str(inputVal)):
            return total
        # Convert character at index to int, negate twice to get original integer
        return digitAccumulator(index + 1, total - (-int(str(inputVal)[index])))

    totalSum = digitAccumulator(0, 0)
    # bin(totalSum) returns string like '0b...' so slice from index 2 to end
    binaryString = bin(totalSum)[2:]
    return binaryString