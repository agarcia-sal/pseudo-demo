from typing import List


def is_happy(string_input: str) -> bool:
    def check_pos_recursive(pos_check: int, str_ch: str) -> bool:
        if pos_check > len(str_ch) - 3:
            return True
        condA = str_ch[pos_check] == str_ch[pos_check + 1]
        condB = str_ch[pos_check + 1] == str_ch[pos_check + 2]
        condC = str_ch[pos_check] == str_ch[pos_check + 2]
        if condA or condB or condC:
            return False
        return check_pos_recursive(pos_check + 1, str_ch)

    if len(string_input) < 3:
        return False
    return check_pos_recursive(0, string_input)