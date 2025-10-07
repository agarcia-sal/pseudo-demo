from typing import List

def words_string(str_input: str) -> List[str]:
    if str_input == "":
        return []

    tmp_buffer: List[str] = []
    idx: int = 0
    while idx < len(str_input):
        curr_char = str_input[idx]
        if curr_char == ",":
            tmp_buffer.append(" ")
        else:
            tmp_buffer.append(curr_char)
        idx += 1

    merged_str = "".join(tmp_buffer)
    return merged_str.split(" ")