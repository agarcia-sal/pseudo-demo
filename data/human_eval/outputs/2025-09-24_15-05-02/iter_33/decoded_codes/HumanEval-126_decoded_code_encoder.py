from collections import Counter
from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    count_digit = Counter(list_of_numbers)
    if any(count > 2 for count in count_digit.values()):
        return False
    return all(list_of_numbers[i - 1] <= list_of_numbers[i] for i in range(1, len(list_of_numbers)))