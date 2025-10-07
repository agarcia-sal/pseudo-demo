from typing import List


def words_string(arg_string: str) -> List[str]:
    if arg_string == "":
        return []

    new_chars: List[str] = []

    idx = 0
    while idx < len(arg_string):
        curr_char = arg_string[idx]
        if curr_char == ",":
            new_chars.append(" ")
        else:
            new_chars.append(curr_char)
        idx += 1

    combined_str = ""
    pos = 0
    while pos < len(new_chars):
        combined_str += new_chars[pos]
        pos += 1

    result_list = combined_str.split()
    return result_list