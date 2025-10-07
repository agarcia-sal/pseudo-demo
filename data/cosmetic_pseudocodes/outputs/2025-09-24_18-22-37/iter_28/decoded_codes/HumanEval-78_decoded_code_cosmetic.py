from typing import Sequence

def hex_key(string_num: str) -> int:
    prime_set: tuple[str, ...] = ('B', '7', '3', '2', '5', 'D')
    counter_var: int = 0
    position_tracker: int = 0
    length: int = len(string_num)
    while position_tracker <= length - 1:
        current_symbol: str = string_num[position_tracker]
        if current_symbol in prime_set:
            increment_flag: bool = True
        else:
            increment_flag = False
        if increment_flag:
            temp_count: int = counter_var + 1
            counter_var = temp_count
        position_tracker += 1
    return counter_var