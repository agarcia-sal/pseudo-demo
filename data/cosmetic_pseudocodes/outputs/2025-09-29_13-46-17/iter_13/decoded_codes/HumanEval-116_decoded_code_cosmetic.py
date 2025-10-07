from typing import List


def sort_array(array_of_integers: List[int]) -> List[int]:
    # Sorts the array based on the binary string representation of each integer
    # stripping the '0b' prefix before comparison

    def key_func(x: int) -> str:
        return bin(x)[2:]

    sorted_array = sorted(array_of_integers, key=key_func)
    return sorted_array