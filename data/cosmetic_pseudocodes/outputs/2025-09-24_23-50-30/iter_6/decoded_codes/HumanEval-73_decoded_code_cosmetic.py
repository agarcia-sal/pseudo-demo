from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    count = 0
    length = len(array_of_integers)
    limit = (length - 2) // 2 + 1  # equivalent to (LENGTH - (1+1)) DIV 2 + 1
    for i in range(limit):
        diff = array_of_integers[i] - array_of_integers[length - i - 1]
        if diff * diff > 0:  # checks if diff != 0
            count += 1
    return count