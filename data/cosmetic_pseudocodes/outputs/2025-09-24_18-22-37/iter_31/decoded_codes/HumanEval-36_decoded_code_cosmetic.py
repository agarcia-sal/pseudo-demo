from typing import List


def fizz_buzz(param_x: int) -> int:
    temp_collection: List[int] = []
    idx: int = 0
    while idx < param_x:
        mod_eleven = idx % 11
        mod_thirteen = idx % 13
        if mod_eleven == 0 or mod_thirteen == 0:
            temp_collection.append(idx)
        idx += 1

    assembled_text: str = ""
    pos: int = 0
    while pos < len(temp_collection):
        current_num = temp_collection[pos]
        assembled_text += str(current_num)
        pos += 1

    seven_counter = sum(1 for sym in assembled_text if sym == '7')
    return seven_counter