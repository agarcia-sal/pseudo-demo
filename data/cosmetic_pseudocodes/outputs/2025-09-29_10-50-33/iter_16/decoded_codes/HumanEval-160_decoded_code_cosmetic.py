from typing import Sequence, Union

def do_algebra(operators_seq: Sequence[str], operands_seq: Sequence[Union[int, float, str]]) -> str:
    expr_parts = [str(operands_seq[0])]
    index = 1
    while index <= len(operators_seq):
        expr_parts.append(operators_seq[index - 1] + str(operands_seq[index]))
        index += 1
    final_expr = "".join(expr_parts)
    return final_expr