from typing import List, Union
import operator
import ast
import math

def do_algebra(list_of_operators: List[str], list_of_operands: List[Union[int, float]]) -> float:
    expression_parts = [str(list_of_operands[0])]
    for operator_symbol, operand_value in zip(list_of_operators, list_of_operands[1:]):
        expression_parts.append(operator_symbol)
        expression_parts.append(str(operand_value))
    expression_string = ''.join(expression_parts)

    # Safely evaluate the arithmetic expression using ast parsing
    def eval_expr(expr: str) -> float:
        allowed_nodes = {
            ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Load,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd,
            ast.Mod, ast.FloorDiv, ast.Constant,
            # Optionally extend for math functions if needed
        }

        def _eval(node):
            if type(node) not in allowed_nodes:
                raise ValueError(f"Disallowed expression: {type(node).__name__}")
            if isinstance(node, ast.Expression):
                return _eval(node.body)
            elif isinstance(node, ast.Constant):  # For Python 3.8+
                if isinstance(node.value, (int, float)):
                    return node.value
                else:
                    raise ValueError("Non-numeric constant not allowed")
            elif isinstance(node, ast.Num):  # For backward compatibility with older Python
                return node.n
            elif isinstance(node, ast.BinOp):
                left = _eval(node.left)
                right = _eval(node.right)
                op_type = type(node.op)
                ops = {
                    ast.Add: operator.add,
                    ast.Sub: operator.sub,
                    ast.Mult: operator.mul,
                    ast.Div: operator.truediv,
                    ast.Pow: operator.pow,
                    ast.Mod: operator.mod,
                    ast.FloorDiv: operator.floordiv,
                }
                if op_type in ops:
                    return ops[op_type](left, right)
                else:
                    raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
            elif isinstance(node, ast.UnaryOp):
                operand = _eval(node.operand)
                op_type = type(node.op)
                if op_type is ast.UAdd:
                    return +operand
                elif op_type is ast.USub:
                    return -operand
                else:
                    raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
            else:
                raise ValueError(f"Unsupported expression node: {type(node).__name__}")

        parsed = ast.parse(expr, mode='eval')
        return _eval(parsed)

    return eval_expr(expression_string)