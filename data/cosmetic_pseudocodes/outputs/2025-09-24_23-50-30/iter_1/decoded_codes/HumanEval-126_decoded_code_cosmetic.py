from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_digit: dict[int, int] = {}
    for num in list_of_numbers:
        count_digit[num] = count_digit.get(num, 0) + 1
    if any(count > 2 for count in count_digit.values()):
        return False
    return all(list_of_numbers[i - 1] <= list_of_numbers[i] for i in range(1, len(list_of_numbers)))