from typing import List, Optional


def longest(arr_of_texts: List[str]) -> Optional[str]:
    if arr_of_texts:
        len_max: int = 0
        idx_i: int = 0
        while idx_i < len(arr_of_texts):
            curr_len: int = len(arr_of_texts[idx_i])
            if curr_len > len_max:
                len_max = curr_len
            idx_i += 1

        idx_k: int = 0
        while idx_k < len(arr_of_texts):
            current_str: str = arr_of_texts[idx_k]
            if len(current_str) == len_max:
                return current_str
            idx_k += 1
    else:
        return None