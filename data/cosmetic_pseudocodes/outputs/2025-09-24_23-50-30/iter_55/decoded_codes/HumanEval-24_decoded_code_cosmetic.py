from typing import Optional


def largest_divisor(integer_n: int) -> Optional[int]:
    stack_x: list[int] = []
    counter_y: int = 0

    while counter_y < integer_n:
        stack_x.append(counter_y)
        counter_y += 1

    stack_x.reverse()

    index_z: int = 0
    while index_z < len(stack_x):
        element_w: int = stack_x[index_z]

        if element_w != 0 and integer_n % element_w == 0:
            return element_w

        index_z += 1
    return None