from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    def collect_largest_elements(
        sorted_arr: List[int], count: int, index: int, collected: List[int]
    ) -> List[int]:
        if index < 0 or count == 0:
            return collected
        return collect_largest_elements(
            sorted_arr, count - 1, index - 1, [sorted_arr[index]] + collected
        )

    if positive_integer_k == 0:
        return []

    sorted_nums = array_of_integers[:]
    sorted_nums.sort()  # natural ascending sort, stable and efficient

    return collect_largest_elements(sorted_nums, positive_integer_k, len(sorted_nums) - 1, [])