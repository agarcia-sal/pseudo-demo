from typing import Callable

def change_base(integer_x: int, integer_base: int) -> str:
    def loop_body(current_val: int, acc: str) -> str:
        if current_val <= 0:
            return acc
        mod_char = str(current_val - (current_val // integer_base) * integer_base)
        new_acc = mod_char + acc
        next_val = current_val // integer_base
        return loop_body(next_val, new_acc)

    return loop_body(integer_x, "")