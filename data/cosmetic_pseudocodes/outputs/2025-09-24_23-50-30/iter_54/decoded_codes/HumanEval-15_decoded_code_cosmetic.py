from typing import List


def string_sequence(inputCount: int) -> str:
    def helper(accumulatedList: List[str], currentIndex: int) -> str:
        if currentIndex > inputCount:
            return " ".join(accumulatedList)
        else:
            return helper(accumulatedList + [str(currentIndex)], currentIndex + 1)

    return helper([], 0)