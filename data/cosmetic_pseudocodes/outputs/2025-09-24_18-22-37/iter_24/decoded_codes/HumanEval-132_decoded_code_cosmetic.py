from typing import List


def is_nested(strng: str) -> bool:
    open_idxs: List[int] = []
    close_idxs: List[int] = []
    curr_idx: int = 0
    length: int = len(strng)

    while curr_idx < length:
        curr_char: str = strng[curr_idx]
        if curr_char == '[':
            open_idxs.append(curr_idx)
        else:
            close_idxs.append(curr_idx)
        curr_idx += 1

    close_idxs.reverse()

    counter_var: int = 0
    pos_var: int = 0
    close_leng: int = len(close_idxs)

    ptr_var: int = 0
    while ptr_var < len(open_idxs):
        current_open_idx: int = open_idxs[ptr_var]

        if pos_var < close_leng and current_open_idx < close_idxs[pos_var]:
            counter_var += 1
            pos_var += 1

        ptr_var += 1

    result_flag: bool = False
    if counter_var >= 2:
        result_flag = True

    return result_flag