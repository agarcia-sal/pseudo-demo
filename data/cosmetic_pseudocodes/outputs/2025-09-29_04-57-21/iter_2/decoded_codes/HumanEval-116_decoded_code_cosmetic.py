from typing import List, Tuple

def sort_array(array_of_integers: List[int]) -> List[int]:
    intermediate_sorted: List[int] = sorted(array_of_integers)  # sort ascending by natural order
    counts_map: List[Tuple[int, int]] = []
    for each_val in intermediate_sorted:
        binary_str: str = bin(each_val)[2:]  # convert to binary string without '0b' prefix
        ones_count: int = binary_str.count('1')  # count number of '1's in the binary representation
        counts_map.append((each_val, ones_count))
    counts_map.sort(key=lambda x: x[1])  # sort by ones_count ascending
    result_arr: List[int] = [item[0] for item in counts_map]
    return result_arr