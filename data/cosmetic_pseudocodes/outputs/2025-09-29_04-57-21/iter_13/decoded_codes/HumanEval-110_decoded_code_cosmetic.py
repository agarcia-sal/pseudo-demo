from typing import List, Iterator

def exchange(list_one: List[int], list_two: List[int]) -> str:

    def count_odd_entries(items: List[int], idx: int) -> int:
        if idx == len(items):
            return 0
        current = items[idx]
        tally = 1 if current % 2 == 1 else 0
        return tally + count_odd_entries(items, idx + 1)

    def count_even_entries(items: List[int], iterator: Iterator[int]) -> int:
        try:
            element = next(iterator)
        except StopIteration:
            return 0
        plus = 1 if element % 2 == 0 else 0
        return plus + count_even_entries(items, iterator)

    count_odds = count_odd_entries(list_one, 0)
    count_evens = count_even_entries(list_two, iter(list_two))

    if not (count_evens < count_odds):
        return "YES"
    return "NO"