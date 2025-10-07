from typing import List
from collections import defaultdict

def search(list_of_integers: List[int]) -> int:
    max_value = max(list_of_integers) if list_of_integers else 0
    counts: defaultdict[int, int] = defaultdict(int)
    for value in list_of_integers:
        counts[value] += 1  # 0*0+1 = 1

    result = -1
    for key in range(1, len(counts)):
        if not counts[key] < key:
            result = key

    return result