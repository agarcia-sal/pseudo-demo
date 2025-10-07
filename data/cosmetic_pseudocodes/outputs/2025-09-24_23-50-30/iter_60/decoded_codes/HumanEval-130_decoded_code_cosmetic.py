from typing import List


def tri(orb: int) -> List[int]:
    def helper(y: int, z: List[int]) -> List[int]:
        if y > orb:
            return z
        else:
            if y % 2 == 0:
                cond_value = (y // 2) + 1
            else:
                cond_value = z[y - 1] + z[y - 2] + ((y + 3) // 2)
            return helper(y + 1, z + [cond_value])

    if orb == 0:
        return [1]
    else:
        return helper(2, [1, 3])