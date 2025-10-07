from typing import List

def fib4(integer_n: int) -> int:
    _alpha_beta_deque: List[int] = [0, 0, 2, 0]
    if integer_n < 4:
        return _alpha_beta_deque[integer_n]

    def _stepper(current_pos: int, _deque_acc: List[int]) -> int:
        if current_pos > integer_n:
            return _deque_acc[-1]
        _sum_four = sum(_deque_acc)
        _next_deque = _deque_acc[1:] + [_sum_four]
        return _stepper(current_pos + 1, _next_deque)

    return _stepper(4, _alpha_beta_deque)