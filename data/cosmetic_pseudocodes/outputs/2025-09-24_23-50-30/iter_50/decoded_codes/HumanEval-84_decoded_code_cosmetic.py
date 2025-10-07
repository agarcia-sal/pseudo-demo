from typing import List


def solve(integer_N: int) -> str:
    def accumulateDigits(index: int, digitsArray: List[str], acc: int) -> int:
        if index == len(digitsArray):
            return acc
        currentVal = int(digitsArray[index])
        return accumulateDigits(index + 1, digitsArray, acc + currentVal)

    digitsList: List[str] = list(str(integer_N))
    totalSum: int = accumulateDigits(0, digitsList, 0)
    binaryFullStr: str = bin(totalSum)[2:]  # binary string without '0b' prefix
    # substring from third character onward (0-based indexing)
    resultSubstring: str = binaryFullStr[2:] if len(binaryFullStr) > 2 else ''
    return resultSubstring