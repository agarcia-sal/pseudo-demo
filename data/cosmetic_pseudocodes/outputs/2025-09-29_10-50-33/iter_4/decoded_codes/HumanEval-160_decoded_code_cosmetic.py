from typing import List

def do_algebra(array_of_ops: List[str], sequence_of_vals: List[int]) -> int:
    result_expr: str = str(sequence_of_vals[0])

    def append_op_val(idx: int) -> None:
        nonlocal result_expr
        if idx >= len(sequence_of_vals):
            return
        current_op: str = array_of_ops[idx - 1]
        current_val: int = sequence_of_vals[idx]
        appender: str = current_op + str(current_val)
        result_expr += appender
        append_op_val(idx + 1)

    append_op_val(1)
    return eval(result_expr)