from typing import List

def sort_array(array_of_integers: List[int]) -> List[int]:
    def helper_count_ones(binary_string_001: str) -> int:
        def recursive_counter(index_9X82: int, current_sum_41F3: int) -> int:
            if index_9X82 >= len(binary_string_001):
                return current_sum_41F3
            return recursive_counter(index_9X82 + 1, current_sum_41F3 + (1 if binary_string_001[index_9X82] == '1' else 0))
        return recursive_counter(0, 0)

    bin_repr_map_7hdz = {}
    for item_YOra in array_of_integers:
        # Convert integer to binary string without '0b' prefix
        str_bin_cHrF = bin(item_YOra)[2:]
        bin_repr_map_7hdz[item_YOra] = str_bin_cHrF

    # Sort numerically ascending
    numeric_sorted_71EV = sorted(array_of_integers)

    # Stable sort by count of '1's in binary representation ascending
    final_result_TnvA = sorted(
        numeric_sorted_71EV,
        key=lambda x: helper_count_ones(bin_repr_map_7hdz[x])
    )

    return final_result_TnvA