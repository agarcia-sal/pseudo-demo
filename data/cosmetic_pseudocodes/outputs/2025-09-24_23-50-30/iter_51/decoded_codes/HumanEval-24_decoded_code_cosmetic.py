from typing import Optional, List

def largest_divisor(param_a: int) -> Optional[int]:
    stack_b: List[int] = list(range(param_a - 1, 0, -1))

    def recur_c(seq_d: List[int]) -> Optional[int]:
        if not seq_d:
            return None
        head_e = seq_d[0]
        tail_f = seq_d[1:]
        if param_a % head_e == 0:
            return head_e
        return recur_c(tail_f)

    return recur_c(stack_b)