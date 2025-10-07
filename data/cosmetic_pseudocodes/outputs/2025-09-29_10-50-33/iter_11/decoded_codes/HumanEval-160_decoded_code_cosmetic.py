from typing import Sequence, Union, Any


def do_algebra(sequence_of_operators: Sequence[str], sequence_of_operands: Sequence[Any]) -> Any:
    composed_expression = str(sequence_of_operands[0])
    idx = 1
    while idx < len(sequence_of_operators) + 1:
        current_operator = sequence_of_operators[idx - 1]
        current_operand = sequence_of_operands[idx]
        # Append operand then operator to the expression string
        composed_expression += str(current_operand) + current_operator
        idx += 1
    # Evaluate the composed expression and return the result
    return eval(composed_expression)