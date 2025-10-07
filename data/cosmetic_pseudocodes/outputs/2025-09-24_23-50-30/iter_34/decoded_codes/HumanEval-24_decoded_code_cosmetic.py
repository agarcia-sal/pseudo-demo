from typing import Optional


def largest_divisor(integer_x: int) -> Optional[int]:
    def find_divisor(integer_y: int, integer_z: int) -> Optional[int]:
        if integer_z < 1:
            return None
        if integer_y % integer_z == 0:
            return integer_z
        return find_divisor(integer_y, integer_z - 1)

    return find_divisor(integer_x, integer_x - 1)