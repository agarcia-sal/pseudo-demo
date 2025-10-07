from typing import List

def words_string(param_str: str) -> List[str]:
    if param_str == "":
        return []
    arr_chars: List[str] = []
    idx: int = 0
    len_str: int = len(param_str)

    while idx < len_str:
        curr_char: str = param_str[idx]
        if curr_char == ",":
            arr_chars.append(" ")
        else:
            arr_chars.append(curr_char)
        idx += 1

    stitched_string: str = ""
    pos: int = 0
    total_chars: int = len(arr_chars)

    while pos < total_chars:
        temp_c: str = arr_chars[pos]
        stitched_string += temp_c
        pos += 1

    out_list: List[str] = stitched_string.split()
    return out_list