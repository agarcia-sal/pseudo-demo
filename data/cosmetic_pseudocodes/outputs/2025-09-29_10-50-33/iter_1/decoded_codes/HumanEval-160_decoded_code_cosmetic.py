from typing import List, Union

def do_algebra(list_of_operators: List[str], list_of_operands: List[Union[int, float]]) -> float:
    expression_parts: List[str] = [str(list_of_operands[0])]
    for i in range(len(list_of_operators)):
        expression_parts.append(list_of_operators[i])
        expression_parts.append(str(list_of_operands[i + 1]))
    full_expression = ''.join(expression_parts)
    return eval(full_expression)