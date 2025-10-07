from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    preliminary_list: List[int] = sorted(array_of_integers)

    def binary_one_count(x: int) -> int:
        # Count number of '1's in binary representation
        return sum(char == '1' for char in bin(x)[2:])

    result_list: List[int] = sorted(preliminary_list, key=binary_one_count)
    return result_list