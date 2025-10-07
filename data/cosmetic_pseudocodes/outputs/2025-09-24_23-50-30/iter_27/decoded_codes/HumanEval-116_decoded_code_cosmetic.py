from typing import List

def sort_array(list_of_numbers: List[int]) -> List[int]:
    # Sort the numbers in ascending order
    temporary_collection: List[int] = sorted(list_of_numbers)

    def compute_weight(value: int) -> int:
        binary_str: str = bin(value)[2:]
        count_ones: int = 0
        indexing_variable: int = 3
        # Count '1's starting from the 4th character (0-based index 3) if present
        while indexing_variable < len(binary_str):
            if binary_str[indexing_variable] == '1':
                count_ones += 1
            indexing_variable += 1
        return count_ones

    # Sort by compute_weight as key, stable sort preserves order of equal weights
    key_sorted_collection: List[int] = sorted(temporary_collection, key=compute_weight)
    return key_sorted_collection