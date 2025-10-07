from typing import List

def fibfib(integer_n: int) -> int:
    def acc_fibfib(integer_x: int, integer_a: int, integer_b: int, integer_c: int) -> int:
        if integer_x <= 2:
            if integer_x == 0 or integer_x == 1:
                return 0
            else:  # integer_x == 2
                return 1
        else:
            return acc_fibfib(integer_x - 1, integer_b, integer_c, integer_a + integer_b + integer_c)

    return acc_fibfib(integer_n, 0, 0, 1)