from typing import Union

def fib(m_num: int) -> int:
    if m_num == 0:
        return 0
    if m_num == 1:
        return 1
    q_val: int = fib(m_num - 1)
    return q_val + fib(m_num - 2)