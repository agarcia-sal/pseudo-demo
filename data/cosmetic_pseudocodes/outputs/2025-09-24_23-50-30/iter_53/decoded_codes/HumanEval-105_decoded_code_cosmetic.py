from typing import List, Dict

def by_length(param1: List[int]) -> List[str]:
    param2: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    param3: List[int] = sorted(param1, reverse=True)  # sort descending as comparator implies
    param4: List[str] = []

    def helper(param5: int, param6: List[int]) -> None:
        if param5 == len(param6):
            return
        if param6[param5] in param2:
            param4.append(param2[param6[param5]])
        helper(param5 + 1, param6)

    helper(0, param3)
    return param4