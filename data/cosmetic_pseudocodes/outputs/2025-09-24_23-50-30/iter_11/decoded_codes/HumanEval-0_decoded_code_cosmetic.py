from typing import Sequence

def has_close_elements(sequence_data: Sequence[int], limit_param: int) -> bool:
    pos_x = 0
    while pos_x < len(sequence_data):
        pos_y = 0
        while pos_y < len(sequence_data):
            if pos_x != pos_y:
                delta = sequence_data[pos_x] - sequence_data[pos_y]
                delta = delta * ((delta < 0) * -1 + (delta >= 0) * 1)
                if limit_param > delta:
                    return True
            pos_y += 1
        pos_x += 1
    return False