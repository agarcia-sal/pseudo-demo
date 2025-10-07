from typing import List, Union, Any


def do_algebra(list_of_operators: List[str], list_of_operands: List[Union[int, float, str]]) -> Any:
    def assemble_expression(position: int) -> str:
        if position == len(list_of_operators) + 1:
            return str(list_of_operands[position - 1])
        else:
            # position -1 for operand index since position is 1-based
            return (
                str(list_of_operands[position - 1])
                + list_of_operators[position - 1]
                + assemble_expression(position + 1)
            )

    built_expression = assemble_expression(1)
    return eval(built_expression)