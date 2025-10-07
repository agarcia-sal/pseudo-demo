from typing import List

def maximum(numbers: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    sorted_numbers: List[int] = []
    for item in numbers:
        # Insert item into sorted_numbers preserving non-decreasing order
        left, right = 0, len(sorted_numbers)
        while left < right:
            mid = (left + right) // 2
            if sorted_numbers[mid] < item:
                left = mid + 1
            else:
                right = mid
        sorted_numbers.insert(left, item)
    cutoff_index = len(sorted_numbers) - count
    return sorted_numbers[cutoff_index:]