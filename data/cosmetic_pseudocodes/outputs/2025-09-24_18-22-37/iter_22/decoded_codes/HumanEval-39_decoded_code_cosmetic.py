from math import sqrt, floor
from typing import List


def prime_fib(m_param: int) -> int:
    def is_prime(q_param: int) -> bool:
        if q_param < 2:
            return False
        limit_val = min(floor(sqrt(q_param)) + 1, q_param - 1)
        for idx_val in range(2, limit_val + 1):
            if q_param % idx_val == 0:
                return False
        return True

    fib_list: List[int] = [0, 1]

    while True:
        a_temp = fib_list[-2]
        b_temp = fib_list[-1]
        c_temp = a_temp + b_temp
        fib_list.append(c_temp)

        if is_prime(c_temp):
            m_param -= 1

        if m_param == 0:
            return c_temp