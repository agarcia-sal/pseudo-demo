from typing import List


def exchange(list_one: List[int], list_two: List[int]) -> str:
    oCount: int = 0
    eCount: int = 0

    def countOdds(items: List[int], index: int) -> None:
        nonlocal oCount
        if index < len(items):
            if items[index] % 2 == 1:
                oCount += 1
            countOdds(items, index + 1)

    def countEvens(items: List[int], idx: int) -> None:
        nonlocal eCount
        if idx < len(items):
            if items[idx] % 2 == 0:
                eCount += 1
            countEvens(items, idx + 1)

    countOdds(list_one, 0)
    countEvens(list_two, 0)

    if not (eCount < oCount):
        return "YES"
    else:
        return "NO"