from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    preliminary_sorted = sorted(array_of_integers)

    def count_ones(number: int) -> int:
        # Count '1's in the binary representation skipping '0b'
        return sum(ch == '1' for ch in bin(number)[2:])

    result: List[int] = []
    for each_element in preliminary_sorted:
        each_ones = count_ones(each_element)
        inserted = False
        for i, val in enumerate(result):
            val_ones = count_ones(val)
            if each_ones < val_ones or (each_ones == val_ones and each_element < val):
                result.insert(i, each_element)
                inserted = True
                break
        if not inserted:
            result.append(each_element)
    return result