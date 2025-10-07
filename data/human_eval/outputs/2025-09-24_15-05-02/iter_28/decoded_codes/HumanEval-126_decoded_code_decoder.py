from typing import List


def is_sorted(list_of_numbers: List[int]) -> bool:
    count_digit = {number: 0 for number in list_of_numbers}
    for number in list_of_numbers:
        count_digit[number] += 1
    if any(count_digit[number] > 2 for number in list_of_numbers):
        return False
    return all(list_of_numbers[i - 1] <= list_of_numbers[i] for i in range(1, len(list_of_numbers)))