from typing import List, Dict


def sort_array(sigma: List[int]) -> List[int]:
    forward_sorted: List[int] = []
    if len(sigma) > 0:
        forward_sorted = [sigma[0]]
        temp_iota: int = 1
        while temp_iota < len(sigma):
            forward_sorted.append(sigma[temp_iota])
            temp_iota += 1
    temp_jived: List[int] = sorted(forward_sorted)
    final_result: Dict[int, int] = {}
    idx_temp: int = 0
    while idx_temp < len(temp_jived):
        element_var: int = temp_jived[idx_temp]
        bin_string: str = bin(element_var)
        bin_trimmed: str = bin_string[2:]  # remove '0b' prefix
        count_ones: int = 0
        indx_bin: int = 0
        while indx_bin < len(bin_trimmed):
            if bin_trimmed[indx_bin] == "1":
                count_ones += 1
            indx_bin += 1
        final_result[element_var] = count_ones
        idx_temp += 1
    # Extract list sorted by count_ones; stable sort by ones count then by element value 
    sorted_by_ones: List[int] = sorted(final_result.keys(), key=lambda x: (final_result[x], x))
    return sorted_by_ones