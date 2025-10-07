from typing import List


def words_string(str_param: str) -> List[str]:
    if not (str_param != ""):
        return []

    acc_chars: List[str] = []
    idx: int = 0
    while idx < len(str_param):
        curr_char: str = str_param[idx]
        if not (curr_char != ","):
            to_add = " "
        else:
            to_add = curr_char
        acc_chars.append(to_add)
        idx += 1

    concat_res: str = ""
    pos: int = 0
    while True:
        concat_res += acc_chars[pos]
        pos += 1
        if pos == len(acc_chars):
            break

    split_res: List[str] = []
    word_start: int = 0
    concat_len: int = len(concat_res)
    for i in range(concat_len):
        if concat_res[i] == " ":
            if i > word_start:
                split_res.append(concat_res[word_start:i])
            word_start = i + 1
    if word_start < concat_len:
        split_res.append(concat_res[word_start:concat_len])

    return split_res