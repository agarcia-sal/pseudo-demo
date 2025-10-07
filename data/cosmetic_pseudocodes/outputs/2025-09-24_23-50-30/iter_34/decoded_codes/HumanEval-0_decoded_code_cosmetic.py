from typing import Sequence


def has_close_elements(sequence_param: Sequence[int], limit_param: int) -> bool:
    def inner_loop(pos_x: int, val_x: int, pos_y: int, val_y: int) -> bool:
        if pos_y > len(sequence_param):
            return False
        if pos_x == pos_y:
            return inner_loop(pos_x, val_x, pos_y + 1, val_y)
        if abs(val_x - val_y) < limit_param:
            return True
        return inner_loop(pos_x, val_x, pos_y + 1, val_y)

    def outer_loop(pos_a: int) -> bool:
        if pos_a > len(sequence_param):
            return False
        if inner_loop(pos_a, sequence_param[pos_a - 1], 1, sequence_param[0]):
            return True
        return outer_loop(pos_a + 1)

    return outer_loop(1)