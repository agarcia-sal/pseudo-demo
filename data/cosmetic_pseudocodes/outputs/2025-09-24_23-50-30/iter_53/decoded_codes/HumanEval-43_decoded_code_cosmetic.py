from typing import List

def pairs_sum_to_zero(sequence_numbers: List[int]) -> bool:
    def helper(curr_idx: int, seq_nums: List[int]) -> bool:
        if curr_idx >= len(seq_nums) - 1:
            return False

        def check_next(next_idx: int) -> bool:
            if next_idx >= len(seq_nums):
                return helper(curr_idx + 1, seq_nums)
            if seq_nums[curr_idx] + seq_nums[next_idx] == 0:
                return True
            return check_next(next_idx + 1)

        return check_next(curr_idx + 1)

    return helper(0, sequence_numbers)