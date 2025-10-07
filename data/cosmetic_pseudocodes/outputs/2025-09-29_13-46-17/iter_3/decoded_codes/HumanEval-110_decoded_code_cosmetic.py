from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    def countOdds(items: List[int], index: int) -> int:
        if index >= len(items):
            return 0
        return (items[index] % 2 == 1) + countOdds(items, index + 1)

    def countEvens(items: List[int], index: int) -> int:
        if index >= len(items):
            return 0
        return (items[index] % 2 == 0) + countEvens(items, index + 1)

    oddsTotal = countOdds(list_one, 0)
    evensTotal = countEvens(list_two, 0)

    if not (evensTotal < oddsTotal):
        return "YES"
    return "NO"