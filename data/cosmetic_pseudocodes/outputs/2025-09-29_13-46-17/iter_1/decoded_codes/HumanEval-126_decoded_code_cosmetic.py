from typing import List

def is_sorted(list_of_numbers: List[int]) -> bool:
    count_digit: dict[int, int] = {}
    for number in list_of_numbers:
        count_digit[number] = count_digit.get(number, 0) + 1
    if any(count > 2 for count in count_digit.values()):
        return False
    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i - 1] > list_of_numbers[i]:
            return False
    return True