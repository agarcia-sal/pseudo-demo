from typing import List

def smallest_change(list_of_integers: List[int]) -> int:
    changes_required = 0
    n = len(list_of_integers)
    for index in range(n // 2):
        if list_of_integers[index] != list_of_integers[n - index - 1]:
            changes_required += 1
    return changes_required