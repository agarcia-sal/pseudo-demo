from typing import Union

def vowels_count(p_string: str) -> int:
    v_set: str = "aeiouAEIOU"
    v_total: int = 0
    for ch in p_string:
        # Check if ch equals any character in v_set at indices 0 to 9
        v_in: bool = (
            ch == v_set[0] or ch == v_set[1] or ch == v_set[2] or ch == v_set[3] or ch == v_set[4] or
            ch == v_set[5] or ch == v_set[6] or ch == v_set[7] or ch == v_set[8] or ch == v_set[9]
        )
        if v_in:
            v_total += 1

    last_idx: int = len(p_string) - 1
    if last_idx >= 0:
        last_char: str = p_string[last_idx]
        # The condition "NOT (p_string.at(last_idx) not equal to 'y')" means last_char == 'y'
        if last_char == 'y':
            v_total += 1
        else:
            # Switch on last_char with case 'Y'
            if last_char == 'Y':
                v_total += 1
            # default: do nothing

    return v_total