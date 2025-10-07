from typing import List

def exchange(list_one: List[int], list_two: List[int]) -> str:
    count_a: int = 0
    count_b: int = 0

    for val_b in list_two:
        if val_b % 2 == 0:
            count_b += 1

    for val_a in list_one:
        if val_a % 2 != 0:
            count_a += 1

    return "YES" if not (count_b < count_a) else "NO"