from collections import deque
from typing import Deque, List, Union


def do_algebra(queue_of_ops: Deque[str], queue_of_vals: Deque[Union[int, float]]) -> float:
    formula_text = str(queue_of_vals[0])
    index = 1
    while index < len(queue_of_vals):
        operator_char = queue_of_ops[index - 1]
        operand_element = queue_of_vals[index]
        formula_text += operator_char + str(operand_element)
        index += 1
    return eval(formula_text)