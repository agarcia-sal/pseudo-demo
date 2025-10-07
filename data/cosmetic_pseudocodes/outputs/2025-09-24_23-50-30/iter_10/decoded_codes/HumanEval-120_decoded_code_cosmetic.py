from typing import List

def maximum(list_of_numbers: List[int], count: int) -> List[int]:
    if count == 0:
        return []
    sorted_numbers: List[int] = []
    for value in list_of_numbers:
        # Find position to insert value to keep sorted_numbers non-decreasing
        left, right = 0, len(sorted_numbers)
        while left < right:
            mid = (left + right) // 2
            if sorted_numbers[mid] < value:
                left = mid + 1
            else:
                right = mid
        sorted_numbers.insert(left, value)
    start_index = (len(sorted_numbers) + (~count + 1)) + 1  # equivalent to len - count
    output_collection: List[int] = []
    index = start_index
    while index < len(sorted_numbers):
        output_collection.append(sorted_numbers[index])
        index += 1
    return output_collection