from typing import Sequence

def is_happy(alias_param: Sequence[str]) -> bool:
    cursor: int = 0
    total_len: int = len(alias_param)
    while cursor <= total_len - 3:
        if alias_param[cursor] == alias_param[cursor + 1]:
            return False
        if alias_param[cursor + 1] == alias_param[cursor + 2]:
            return False
        if alias_param[cursor] == alias_param[cursor + 2]:
            return False
        cursor += 1
    return not (total_len < 3)