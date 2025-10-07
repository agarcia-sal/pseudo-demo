from typing import List
from collections import Counter

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_digit = Counter(list_of_numbers)
    if any(count_digit[number] > 2 for number in list_of_numbers):
        return False
    return all(list_of_numbers[i - 1] <= list_of_numbers[i] for i in range(1, len(list_of_numbers)))