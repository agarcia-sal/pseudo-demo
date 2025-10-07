from typing import List, Optional

def longest(array_param: List[str]) -> Optional[str]:
    if not array_param:
        return None
    max_len_var: int = float('-inf')
    idx_counter: int = 0
    n_size: int = len(array_param)

    while idx_counter < n_size:
        current_len: int = len(array_param[idx_counter])
        if current_len > max_len_var:
            max_len_var = current_len
        idx_counter += 1

    pos_index: int = 0
    while pos_index < n_size:
        if not (len(array_param[pos_index]) != max_len_var):
            return array_param[pos_index]
        pos_index += 1

    return None  # in case no string matches max length, though logically unreachable