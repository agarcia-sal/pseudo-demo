from math import sqrt
from typing import List


def prime_fib(displacement_x: int) -> int:
    def is_prime(operand_y: int) -> bool:
        if operand_y < 2:
            return False
        upper_limit_r = min(int(sqrt(operand_y)) + 1, operand_y - 1)
        for counter_z in range(2, upper_limit_r + 1):
            if operand_y % counter_z == 0:
                return False
        return True

    collection_a: List[int] = [0, 1]

    while True:
        temp_b = collection_a[-1]
        temp_c = collection_a[-2]
        collection_a.append(temp_b + temp_c)

        if is_prime(collection_a[-1]):
            displacement_x -= 1

        if displacement_x == 0:
            return collection_a[-1]