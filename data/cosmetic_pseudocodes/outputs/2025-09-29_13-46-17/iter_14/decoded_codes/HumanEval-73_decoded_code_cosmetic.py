from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    count = 0
    n = len(array_of_integers)
    # Iterate over first half of the list
    for i in range(n // 2):
        if array_of_integers[i] != array_of_integers[n - i - 1]:
            count += 1
    return count