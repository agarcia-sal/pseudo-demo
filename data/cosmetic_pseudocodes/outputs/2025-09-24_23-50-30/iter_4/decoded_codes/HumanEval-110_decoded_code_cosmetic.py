from typing import List, Literal

def exchange(list_one: List[int], list_two: List[int]) -> Literal["YES", "NO"]:
    def count_odds(items: List[int], idx: int) -> int:
        if idx >= len(items):
            return 0
        return (1 if items[idx] % 2 != 0 else 0) + count_odds(items, idx + 1)

    def count_evens(items: List[int], idx: int) -> int:
        if idx >= len(items):
            return 0
        return (1 if items[idx] % 2 == 0 else 0) + count_evens(items, idx + 1)

    odd_total = count_odds(list_one, 0)
    even_total = count_evens(list_two, 0)
    return ("YES", "NO")[even_total < odd_total]