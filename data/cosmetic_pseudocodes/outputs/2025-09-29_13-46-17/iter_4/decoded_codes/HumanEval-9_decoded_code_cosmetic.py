from typing import List, Optional

def rolling_max(list_of_numbers: List[int]) -> List[int]:
    def recursive_process(sequence: List[int], idx: int, acc_max: Optional[int], accum_result: List[int]) -> List[int]:
        if idx >= len(sequence):
            return accum_result
        curr_candidate = sequence[idx]
        updated_max = curr_candidate if acc_max is None or curr_candidate > acc_max else acc_max
        return recursive_process(sequence, idx + 1, updated_max, accum_result + [updated_max])

    return recursive_process(list_of_numbers, 0, None, [])