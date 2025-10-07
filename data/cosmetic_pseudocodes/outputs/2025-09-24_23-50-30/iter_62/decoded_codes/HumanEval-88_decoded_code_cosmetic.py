from typing import List

def sort_array(container: List[int]) -> List[int]:
    def helper(sequence: List[int]) -> List[int]:
        if len(sequence) == 0:
            return []
        combined_value = sequence[0] + sequence[-1]
        desc_flag = (combined_value % 2 == 0)
        return sorted(sequence, reverse=desc_flag)
    return helper(container)