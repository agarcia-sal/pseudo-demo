from typing import List

def sort_array(collection_of_ints: List[int]) -> List[int]:
    def count_ones(bitstring: str, index: int, acc: int) -> int:
        if index >= len(bitstring):
            return acc
        return count_ones(bitstring, index + 1, acc + (1 if bitstring[index] == '1' else 0))

    def ones_in_binary(number: int) -> int:
        bin_repr = bin(number)
        return count_ones(bin_repr, 2, 0)  # Skip '0b' prefix

    intermediate_sorted: List[int] = sorted(collection_of_ints)
    result_array: List[int] = sorted(intermediate_sorted, key=ones_in_binary)
    return result_array