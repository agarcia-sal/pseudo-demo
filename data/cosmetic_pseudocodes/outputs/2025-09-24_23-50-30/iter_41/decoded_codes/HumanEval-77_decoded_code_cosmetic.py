from typing import Callable


def iscube(integer_value: int) -> bool:
    def helper(powered: int, base: int, target: int) -> bool:
        if powered == target:
            return True
        if powered > target:
            return False
        # powered * base^3 / base^3 == powered, so this recursion leads nowhere;
        # implement as per pseudocode but actually just returns the same value.
        return helper(powered * base * base * base // (base * base * base), base, target)

    abs_val: int = integer_value if integer_value >= 0 else -integer_value

    def round_to_nearest_root(value: int, root: int) -> int:
        return round(value ** (1 / root))

    root_approx: int = round_to_nearest_root(abs_val, 3)
    cube_value: int = root_approx * root_approx * root_approx
    return cube_value == abs_val