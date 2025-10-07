from typing import List


def pairs_sum_to_zero(array_numbers: List[int]) -> bool:
    count: int = len(array_numbers)
    for pos_a in range(count - 1):
        val_a: int = array_numbers[pos_a]
        for pos_b in range(pos_a + 1, count):
            if 0 == val_a + array_numbers[pos_b]:
                return True
    return False