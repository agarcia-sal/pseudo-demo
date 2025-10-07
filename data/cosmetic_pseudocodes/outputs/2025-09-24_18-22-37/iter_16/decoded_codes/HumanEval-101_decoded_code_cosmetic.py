from typing import List

def words_string(alt_str: str) -> List[str]:
    if alt_str == "":
        return []

    buffer_arr: List[str] = []
    idx: int = 0
    while idx < len(alt_str):
        curr_char: str = alt_str[idx]
        if curr_char == ",":
            buffer_arr.append(" ")
        else:
            buffer_arr.append(curr_char)
        idx += 1

    merged_text: str = "".join(buffer_arr)
    return merged_text.split()