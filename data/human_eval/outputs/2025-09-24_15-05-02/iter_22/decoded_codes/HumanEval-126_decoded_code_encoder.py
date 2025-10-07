from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_occurrences: dict[int, int] = {number: 0 for number in list_of_numbers}
    for number in list_of_numbers:
        count_occurrences[number] += 1
    for number in list_of_numbers:
        if count_occurrences[number] > 2:
            return False
    for index in range(1, len(list_of_numbers)):
        if list_of_numbers[index - 1] > list_of_numbers[index]:
            return False
    return True