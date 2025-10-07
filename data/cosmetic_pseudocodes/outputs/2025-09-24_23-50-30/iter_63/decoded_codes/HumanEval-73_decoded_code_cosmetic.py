from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count_differences: int = 0
    limit: int = (len(array_of_integers) // 2) - 1
    current: int = 0

    while current <= limit:
        if array_of_integers[current] != array_of_integers[len(array_of_integers) - 1 - current]:
            count_differences += 1
        current += 1

    return count_differences