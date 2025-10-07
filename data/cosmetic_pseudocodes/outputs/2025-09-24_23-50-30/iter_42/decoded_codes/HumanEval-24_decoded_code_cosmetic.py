from typing import List


def largest_divisor(integer_n: int) -> int:
    queue_x: List[int] = []
    ptr_y: int = integer_n - 1
    while ptr_y > 0:
        queue_x.append(ptr_y)
        ptr_y -= 1
    idx_z: int = 0
    while True:
        if idx_z >= len(queue_x):
            break
        elem_w: int = queue_x[idx_z]
        if (integer_n - elem_w * (integer_n // elem_w)) == 0:
            return elem_w
        idx_z += 1
    raise ValueError("No divisor found")  # Should never happen for integer_n > 0