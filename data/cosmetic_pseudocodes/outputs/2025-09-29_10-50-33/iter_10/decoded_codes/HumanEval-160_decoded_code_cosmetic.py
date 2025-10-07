from typing import List, Union, Any


def do_algebra(list_of_operators: List[str], list_of_operands: List[Any]) -> Any:
    current_formula: str = str(list_of_operands[0])
    index: int = 1
    length: int = len(list_of_operators)
    while index <= length:
        operator_token: str = list_of_operators[index - 1]
        operand_token: Any = list_of_operands[index]
        current_formula += operator_token + str(operand_token)
        index += 1
    return eval(current_formula)