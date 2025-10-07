from typing import Sequence, Union
import operator
import re

def do_algebra(collection_of_symbols: Sequence[str], collection_of_values: Sequence[Union[int, float]]) -> float:
    formula_text = str(collection_of_values[0])
    for index_cursor in range(1, len(collection_of_values)):
        current_symbol = collection_of_symbols[index_cursor - 1]
        current_value = collection_of_values[index_cursor]
        formula_text += current_symbol + str(current_value)
    return _compute_expression(formula_text)

def _compute_expression(expression: str) -> float:
    """
    Safely evaluate a simple arithmetic expression containing numbers and the operators +, -, *, /.
    Does not support parentheses or other operators.
    """
    # Tokenize numbers and operators
    tokens = re.findall(r'\d+\.?\d*|[+\-*/]', expression)
    if not tokens:
        raise ValueError("Empty expression")

    # Convert all tokens which are digits to float
    def to_number(token: str) -> Union[str, float]:
        try:
            return float(token)
        except ValueError:
            return token

    tokens = [to_number(token) for token in tokens]

    # Operator precedence
    precedence = {'*': 2, '/': 2, '+': 1, '-': 1}

    # Shunting Yard algorithm to convert to Reverse Polish Notation (RPN)
    output_queue = []
    operator_stack = []

    for token in tokens:
        if isinstance(token, float):
            output_queue.append(token)
        elif token in precedence:
            while operator_stack and precedence.get(operator_stack[-1], 0) >= precedence[token]:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            raise ValueError(f"Invalid token {token}")

    while operator_stack:
        output_queue.append(operator_stack.pop())

    # Evaluate the RPN expression
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    stack = []
    for token in output_queue:
        if isinstance(token, float):
            stack.append(token)
        else:
            if len(stack) < 2:
                raise ValueError("Invalid syntax")
            b = stack.pop()
            a = stack.pop()
            if token == '/' and b == 0:
                raise ZeroDivisionError("Division by zero")
            result = ops[token](a, b)
            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid syntax")
    return stack[0]