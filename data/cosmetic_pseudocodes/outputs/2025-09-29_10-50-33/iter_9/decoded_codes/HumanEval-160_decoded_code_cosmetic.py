from typing import List


def do_algebra(list_of_operators: List[str], list_of_operands: List[int]) -> str:
    def compose_expression(
        current_concat: str, remaining_ops: List[str], remaining_vals: List[int]
    ) -> str:
        if not remaining_ops or not remaining_vals:
            return current_concat
        top_operator = remaining_ops[0]
        next_operand = remaining_vals[0]
        return compose_expression(
            current_concat + top_operator + str(next_operand),
            remaining_ops[1:],
            remaining_vals[1:],
        )

    initial_fragment = str(list_of_operands[0])
    return compose_expression(initial_fragment, list_of_operators, list_of_operands[1:])