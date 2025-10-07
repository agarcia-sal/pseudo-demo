from typing import List

def common(list1: List[int], list2: List[int]) -> List[int]:
    accumulator: set[int] = set()

    def helper(i: int, j: int) -> None:
        if i > len(list1):
            return
        if j > len(list2):
            helper(i + 1, 1)
        else:
            val1 = list1[i - 1]
            val2 = list2[j - 1]
            if val1 == val2:
                accumulator.add(val1)
            helper(i, j + 1)

    helper(1, 1)
    return sorted(accumulator)