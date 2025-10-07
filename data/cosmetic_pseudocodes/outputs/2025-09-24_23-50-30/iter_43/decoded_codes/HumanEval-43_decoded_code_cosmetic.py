from typing import List


def pairs_sum_to_zero(array_of_numbers: List[int]) -> bool:
    cursor_a = 0
    length = len(array_of_numbers)
    while cursor_a < length - 1:
        cursor_b = cursor_a + 1
        while cursor_b < length:
            if array_of_numbers[cursor_a] + array_of_numbers[cursor_b] == 0:
                return True
            cursor_b += 1
        cursor_a += 1
    return False