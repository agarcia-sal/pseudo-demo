from typing import List

def sort_array(arr: List[int]) -> List[int]:
    def key_function(x: int) -> int:
        binary_string = bin(x)
        binary_substring = binary_string[2:-1] if len(binary_string) > 3 else ''
        count_ones = 0
        i = 0
        while i < len(binary_substring):
            if binary_substring[i] == '1':
                count_ones += 1
            i += 1
        return count_ones

    sorted_arr = sorted(arr)
    result = sorted(sorted_arr, key=key_function)
    return result