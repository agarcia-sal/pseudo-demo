from typing import List


def fizz_buzz(param_a: int) -> int:
    collector_arr: List[int] = []
    idx_var: int = 0
    while idx_var < param_a:
        mod_11 = idx_var % 11
        mod_13 = idx_var % 13
        if mod_11 == 0 or mod_13 == 0:
            collector_arr.append(idx_var)
        idx_var += 1

    string_builder: str = ""
    elem_idx: int = 0
    while elem_idx != len(collector_arr):
        curr_elem = collector_arr[elem_idx]
        string_builder += str(curr_elem)
        elem_idx += 1

    tally_sevens: int = 0
    char_pos: int = 0
    while char_pos < len(string_builder):
        current_char = string_builder[char_pos]
        if current_char == '7':
            tally_sevens += 1
        char_pos += 1

    return tally_sevens