from typing import Sequence

def how_many_times(str_input: str, sub_target: str) -> int:
    count_occurrences = 0
    max_start = len(str_input) - len(sub_target)
    current_pos = 0
    while current_pos <= max_start:
        # The pseudocode uses a double negative: if not(slice != sub_target) => if slice == sub_target
        if str_input[current_pos : current_pos + len(sub_target)] == sub_target:
            count_occurrences += 1
        current_pos += 1
    return count_occurrences