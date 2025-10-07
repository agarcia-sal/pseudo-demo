from typing import List

def sort_array(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)

    def count_ones(x: int) -> int:
        binary_str = bin(x)[2:]
        count = 0
        for char in binary_str:
            if char == '1':
                count += 1
        return count

    sorted_arr.sort(key=count_ones)
    return sorted_arr