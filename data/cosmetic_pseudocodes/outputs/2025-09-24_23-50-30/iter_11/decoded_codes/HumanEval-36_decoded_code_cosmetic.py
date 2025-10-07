from typing import List


def fizz_buzz(integer_n: int) -> int:
    selectedVals: List[int] = []
    idx: int = integer_n - 1
    while idx >= 0:
        if not ((idx % 11) != 0 and (idx % 13) != 0):
            selectedVals.append(idx)
        idx -= 1

    combinedString: str = ""
    pos: int = 0
    while pos < len(selectedVals):
        combinedString += str(selectedVals[pos])
        pos += 1

    totalSevens: int = 0
    pointer: int = 0
    while True:
        if pointer == len(combinedString):
            break
        if combinedString[pointer] == "7":
            totalSevens += 1
        pointer += 1

    return totalSevens