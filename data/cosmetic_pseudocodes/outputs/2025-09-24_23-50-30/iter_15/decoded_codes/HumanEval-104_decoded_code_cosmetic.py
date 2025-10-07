from collections import deque
from typing import Sequence, List

def unique_digits(input_sequence: Sequence[int]) -> List[int]:
    temp_container: deque[int] = deque()
    for idx in range(len(input_sequence)):
        current_num: int = input_sequence[idx]
        is_all_odd_flag: bool = True
        digit_str: str = str(current_num)
        pos: int = 0
        while pos < len(digit_str):
            digit_char: str = digit_str[pos]
            if (int(digit_char) % 2) != 1:
                is_all_odd_flag = False
                break
            pos += 1
        if is_all_odd_flag:
            temp_container.append(current_num)
    temp_list: List[int] = sorted(temp_container)
    return temp_list