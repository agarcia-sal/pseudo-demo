from typing import List

def fib4(integer_z: int) -> int:
    list_x: List[int] = [0, 0, 2, 0]

    def recur_y(counter_a: int, list_b: List[int]) -> int:
        if counter_a > integer_z:
            return list_b[3]
        sum_c = list_b[0] + list_b[1] + list_b[2] + list_b[3]
        return recur_y(counter_a + 1, [list_b[1], list_b[2], list_b[3], sum_c])

    if integer_z < 4:
        return list_x[integer_z]

    return recur_y(4, list_x)