from typing import List

def will_it_fly(list_q: List[int], maximum_weight_w: int) -> bool:
    def sum_accumulator(acc: int, rest: List[int]) -> int:
        if not rest:
            return acc
        return sum_accumulator(acc + rest[0], rest[1:])

    if not (maximum_weight_w < sum_accumulator(0, list_q)):
        def compare_indices(left_idx: int, right_idx: int) -> bool:
            if left_idx >= right_idx:
                return True
            if list_q[left_idx] != list_q[right_idx]:
                return False
            return compare_indices(left_idx + 1, right_idx - 1)
        return compare_indices(0, len(list_q) - 1)
    return False