from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    tally_odd: int = 0
    tally_even: int = 0
    iterator_one = iter(list_one)
    while True:
        try:
            current_val = next(iterator_one)
            if current_val % 2 != 0:
                tally_odd += 1
        except StopIteration:
            break
    iterator_two = iter(list_two)
    while True:
        try:
            current_num = next(iterator_two)
            if current_num % 2 == 0:
                tally_even += 1
        except StopIteration:
            break
    if not (tally_even < tally_odd):
        return "YES"
    else:
        return "NO"