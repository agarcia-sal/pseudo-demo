from typing import List, Union

def do_algebra(list_of_operators: List[str], list_of_operands: List[Union[int, float, str]]) -> Union[int, float]:
    i: int = 1
    expression_accumulator: str = str(list_of_operands[0])
    while True:
        if not (i < len(list_of_operators)):
            return expression_to_value_converter(expression_accumulator)
        operator_token: str = list_of_operators[i]
        operand_token: Union[int, float, str] = list_of_operands[i + 1]
        expression_accumulator += str(operand_token) + operator_token
        i += 1

def expression_to_value_converter(expression: str) -> Union[int, float]:
    # Assumes expression is a valid arithmetic expression composed of numbers and operators
    # Evaluate safely using eval with restricted globals
    # For safety, in real use, consider a proper parser or restricted evaluator
    return eval(expression, {"__builtins__": None}, {})