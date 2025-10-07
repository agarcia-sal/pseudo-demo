from typing import List


def digitSum(string_input: str) -> int:
    asciiVals: List[int] = []
    idx: int = 0

    while idx < len(string_input):
        currentChar: str = string_input[idx]
        if 'A' <= currentChar <= 'Z':
            asciiVals.append(ord(currentChar))
        else:
            asciiVals.append(0)
        idx += 1

    def recursiveSum(vals: List[int], pos: int) -> int:
        if pos >= len(vals):
            return 0
        return vals[pos] + recursiveSum(vals, pos + 1)

    return recursiveSum(asciiVals, 0)