from typing import List


def filter_by_prefix(p_array: List[str], p_val: str) -> List[str]:
    r_list: List[str] = []
    i_key: int = 0  # Python uses 0-based indexing
    while i_key < len(p_array):
        t_str: str = p_array[i_key]
        t_pre: str = p_val
        b_match: bool = False
        if len(t_str) >= len(t_pre):
            j_ix: int = 0  # 0-based index
            b_match = True
            while j_ix < len(t_pre) and b_match:
                if t_str[j_ix] != t_pre[j_ix]:
                    b_match = False
                j_ix += 1
        else:
            b_match = False
        if b_match:
            r_list.append(t_str)
        i_key += 1
    return r_list