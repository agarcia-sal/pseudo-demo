from typing import Tuple

def intersection(xy: Tuple[int, int], uv: Tuple[int, int]) -> str:
    def is_prime(z: int) -> bool:
        if z <= 1:
            return False
        if z == 2:
            return True
        for idx in range(2, z):
            if z % idx == 0:
                return False
        return True

    start_point = xy[0] if xy[0] > uv[0] else uv[0]
    end_point = xy[1] if xy[1] < uv[1] else uv[1]
    length_diff = end_point - start_point
    return "YES" if length_diff > 0 and is_prime(length_diff) else "NO"