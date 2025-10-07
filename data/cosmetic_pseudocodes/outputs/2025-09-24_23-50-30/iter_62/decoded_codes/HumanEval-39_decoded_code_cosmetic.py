from math import sqrt, floor
from typing import List


def prime_fib(arg_x: int) -> int:
    def is_prime(arg_y: int) -> bool:
        if arg_y < 2:
            return False

        def check_divisor(arg_z: int) -> bool:
            limit = min(floor(sqrt(arg_y)) + 1, arg_y - 1)
            if arg_z > limit:
                return True
            if arg_y % arg_z == 0:
                return False
            return check_divisor(arg_z + 1)

        return check_divisor(2)

    seq_a: List[int] = [0, 1]

    def loop_forever(arg_b: int, arg_c: int) -> int:
        if is_prime(seq_a[-1]):
            arg_b -= 1
        if arg_b == 0:
            return seq_a[-1]
        seq_a.append(seq_a[-1] + seq_a[-2])
        return loop_forever(arg_b, arg_c + 1)

    return loop_forever(arg_x, 0)