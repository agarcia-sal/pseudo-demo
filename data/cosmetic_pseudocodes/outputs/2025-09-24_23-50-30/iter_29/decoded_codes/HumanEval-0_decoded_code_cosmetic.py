from typing import Sequence

def has_close_elements(sequence_data: Sequence[float], limit_param: float) -> bool:
    cursor_A: int = 0
    cursor_B: int = 0
    length: int = len(sequence_data)
    while cursor_A < length:
        cursor_B = 0
        while cursor_B < length:
            cond_mismatch = (cursor_A != cursor_B)
            cond_limit_check = abs(sequence_data[cursor_A] - sequence_data[cursor_B]) < limit_param
            if cond_mismatch and cond_limit_check:
                return True
            cursor_B += 1
        cursor_A += 1
    return False