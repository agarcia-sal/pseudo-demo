from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    def count_odds(index: int) -> int:
        if index == len(list_one):
            return 0
        current_val = list_one[index]
        return (current_val % 2) + count_odds(index + 1)

    def count_evens(index: int) -> int:
        if index == len(list_two):
            return 0
        current_val = list_two[index]
        # (1 - (current_val % 2)) % 2 ensures a result of 1 if even, 0 if odd
        return ((1 - (current_val % 2)) % 2) + count_evens(index + 1)

    odd_counter = count_odds(0)
    even_counter = count_evens(0)

    return "NO" if odd_counter > even_counter else "YES"