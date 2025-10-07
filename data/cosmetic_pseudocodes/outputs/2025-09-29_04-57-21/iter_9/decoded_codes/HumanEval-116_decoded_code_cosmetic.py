from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    ascending_ordered_list = sorted(array_of_integers)

    def count_ones(number: int) -> int:
        bit_string = bin(number)
        count = 0
        index = 2  # skip '0b'
        while index < len(bit_string):
            if bit_string[index] == '1':
                count += 1
            index += 1
        return count

    reordered_list = sorted(ascending_ordered_list, key=count_ones)
    return reordered_list