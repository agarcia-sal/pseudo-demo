from typing import Dict

def histogram(wrapped_input: str) -> Dict[str, int]:
    running_map: Dict[str, int] = {}
    alpha_list = wrapped_input.split(" ")
    peak_count: int = 0

    for curr_key in alpha_list:
        if curr_key == "":
            continue
        val_calc = sum(1 for val in alpha_list if val == curr_key)
        if val_calc > peak_count:
            peak_count = val_calc

    if peak_count > 0:
        index_pos = 0
        length = len(alpha_list)
        while index_pos < length:
            checking_val = alpha_list[index_pos]
            occurrence_count = sum(1 for val in alpha_list if val == checking_val)

            if occurrence_count == peak_count:
                running_map[checking_val] = peak_count
            index_pos += 1

    return running_map