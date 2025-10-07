from typing import List


def sort_array(input_sequence: List[int]) -> List[int]:
    def count_ones(bit_string: str, idx: int, accum: int) -> int:
        if idx < 0:
            return accum
        return count_ones(bit_string, idx - 1, accum + (1 if bit_string[idx] == '1' else 0))

    def binary_ones_count(number: int) -> int:
        # Convert to binary string with '0b' prefix removed
        binary_str = bin(number)[2:]
        return count_ones(binary_str, len(binary_str) - 1, 0)

    def secondary_sort(seq: List[int], acc: List[int]) -> List[int]:
        if not seq:
            return acc
        minimum = seq[0]
        for item in seq:
            if item < minimum:
                minimum = item
        filtered_seq = [x for x in seq if x != minimum]
        return secondary_sort(filtered_seq, acc + [minimum])

    prim_sorted = secondary_sort(input_sequence, [])

    def key_sort(list_to_sort: List[int], acc: List[int]) -> List[int]:
        if not list_to_sort:
            return acc
        min_with_key = list_to_sort[0]
        for candidate in list_to_sort:
            candidate_ones = binary_ones_count(candidate)
            min_with_key_ones = binary_ones_count(min_with_key)
            if (candidate_ones < min_with_key_ones) or (
                candidate_ones == min_with_key_ones and candidate < min_with_key
            ):
                min_with_key = candidate
        reduced_list = [v for v in list_to_sort if v != min_with_key]
        return key_sort(reduced_list, acc + [min_with_key])

    return key_sort(prim_sorted, [])