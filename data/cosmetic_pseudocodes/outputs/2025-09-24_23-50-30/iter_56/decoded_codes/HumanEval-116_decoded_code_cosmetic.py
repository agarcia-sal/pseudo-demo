from typing import List

def sort_array(fresh_seq: List[int]) -> List[int]:
    def count_ones_in_bin(val: int, acc: int) -> int:
        if val == 0:
            return acc
        return count_ones_in_bin(val // 2, acc + (val % 2))

    arranged_by_value = sorted(fresh_seq)
    arranged_by_ones = sorted(arranged_by_value, key=lambda member: count_ones_in_bin(member, 0))
    return arranged_by_ones