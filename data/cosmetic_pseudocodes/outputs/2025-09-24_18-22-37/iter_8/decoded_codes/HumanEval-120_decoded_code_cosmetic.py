from typing import List

def maximum(collection_of_numbers: List[int], count_limit: int) -> List[int]:
    if count_limit != 0:
        sorted_numbers = sorted(collection_of_numbers)
        start_index = max(len(sorted_numbers) - count_limit, 0)
        return sorted_numbers[start_index:]
    else:
        return []