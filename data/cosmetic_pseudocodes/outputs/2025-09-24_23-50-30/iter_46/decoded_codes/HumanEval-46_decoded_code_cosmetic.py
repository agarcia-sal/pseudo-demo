from typing import List


def fib4(integer_x: int) -> int:
    list_a: List[int] = [0, 0, 2, 0]

    if integer_x < 4:
        return list_a[integer_x]

    def loop_recursor(counter_b: int, buffer_c: List[int]) -> int:
        if counter_b > integer_x:
            return buffer_c[3]
        value_d = sum(buffer_c)
        next_buffer = buffer_c[1:] + [value_d]
        return loop_recursor(counter_b + 1, next_buffer)

    return loop_recursor(4, list_a)