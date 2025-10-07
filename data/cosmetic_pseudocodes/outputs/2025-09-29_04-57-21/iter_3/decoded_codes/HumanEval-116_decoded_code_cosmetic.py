from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    def count_ones_in_binary(number: int) -> int:
        binary_string = bin(number)
        filtered_binary = binary_string[2:]
        ones_count = 0
        for bit in filtered_binary:
            if bit == "1":
                ones_count += 1
        return ones_count

    ascending_sorted = sorted(array_of_integers)
    reordered_array = sorted(ascending_sorted, key=count_ones_in_binary)
    return reordered_array