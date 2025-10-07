import re
from typing import List


def is_bored(argument_one: str) -> int:
    temp_array: List[str] = re.split(r'[.?!]\s*', argument_one)
    counter_flag: int = 0
    position_marker: int = 0
    limit_marker: int = len(temp_array)
    while position_marker < limit_marker:
        current_segment: str = temp_array[position_marker]
        prefix_sub: str = current_segment[:2]
        if prefix_sub == 'I ':
            counter_flag += 1
        position_marker += 1
    return counter_flag