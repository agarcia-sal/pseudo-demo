from typing import Sequence

def is_happy(motion_data: Sequence[int]) -> bool:
    if len(motion_data) < 3:
        return False

    def examine_loop(scan_pos: int, limit_pos: int) -> bool:
        if scan_pos > limit_pos:
            return True
        if (motion_data[scan_pos] == motion_data[scan_pos + 1] or
            motion_data[scan_pos + 1] == motion_data[scan_pos + 2] or
            motion_data[scan_pos] == motion_data[scan_pos + 2]):
            return False
        return examine_loop(scan_pos + 1, limit_pos)

    return examine_loop(0, len(motion_data) - 3)