from typing import Callable

def greatest_common_divisor(integer_a: int, integer_b: int) -> int:
    def CALL_CONTINUATION(cont_x: int, cont_y: int) -> int:
        if cont_y == 0:
            return cont_x
        else:
            return proceed_trampoline(CALL_CONTINUATION, cont_y, cont_x % cont_y)

    def proceed_trampoline(fn: Callable[[int, int], int], arg1: int, arg2: int) -> int:
        return tail_recurse(fn, arg1, arg2)

    def tail_recurse(func: Callable[[int, int], int], param_α: int, param_β: int) -> int:
        def ITERATE(x: int, y: int) -> int:
            if y == 0:
                return x
            else:
                return ITERATE(y, x % y)
        return ITERATE(param_α, param_β)

    return proceed_trampoline(lambda continuation_x, continuation_y: CALL_CONTINUATION(continuation_x, continuation_y), integer_a, integer_b)