from typing import List

def pairs_sum_to_zero(array_of_numbers: List[int]) -> bool:
    def scan_pairs(counter_a: int, counter_b: int) -> bool:
        if counter_a == len(array_of_numbers) - 1:
            return False
        if counter_b == len(array_of_numbers):
            return scan_pairs(counter_a + 1, counter_a + 2)
        if array_of_numbers[counter_a] + array_of_numbers[counter_b] == 0:
            return True
        return scan_pairs(counter_a, counter_b + 1)
    return scan_pairs(0, 1)