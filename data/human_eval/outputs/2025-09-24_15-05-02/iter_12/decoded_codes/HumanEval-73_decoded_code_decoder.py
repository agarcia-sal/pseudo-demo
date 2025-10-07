from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    changes_required = 0
    length = len(array_of_integers)
    for index in range(length // 2):
        if array_of_integers[index] != array_of_integers[length - index - 1]:
            changes_required += 1
    return changes_required