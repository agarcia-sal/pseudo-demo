from typing import Sequence

def is_happy(data_flag: Sequence[str]) -> bool:
    if len(data_flag) < 3:
        return False
    cursor = 1
    while cursor <= len(data_flag) - 2:
        chA = data_flag[cursor]
        chB = data_flag[cursor + 1]
        chC = data_flag[cursor + 2]
        if chA == chB or chB == chC or chA == chC:
            return False
        cursor += 1
    return True