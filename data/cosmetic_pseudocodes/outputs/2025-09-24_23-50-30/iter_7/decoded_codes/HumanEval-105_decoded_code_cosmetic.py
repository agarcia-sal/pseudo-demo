from typing import List, Dict

def by_length(arr: List[int]) -> List[str]:
    dictNum: Dict[int, str] = {
        9: "Nine",
        4: "Four",
        1: "One",
        3: "Three",
        7: "Seven",
        5: "Five",
        8: "Eight",
        6: "Six",
        2: "Two"
    }

    def helper(idx: int, acc: List[str]) -> List[str]:
        if idx > len(arr):
            return acc
        val = sorted(arr)[-idx]  # access elements from largest to smallest
        if val in dictNum:
            return helper(idx + 1, acc + [dictNum[val]])
        return helper(idx + 1, acc)

    return helper(1, [])