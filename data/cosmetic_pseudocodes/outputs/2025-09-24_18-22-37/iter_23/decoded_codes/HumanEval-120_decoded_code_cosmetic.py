from typing import List

def maximum(list_of_numbers: List[int], count_limit: int) -> List[int]:
    if count_limit != 0:
        sorted_numbers = sorted(list_of_numbers)  # sort ascending
        starting_point = max(len(sorted_numbers) - count_limit, 0)
        results_container = sorted_numbers[starting_point:]
        return results_container
    else:
        return []