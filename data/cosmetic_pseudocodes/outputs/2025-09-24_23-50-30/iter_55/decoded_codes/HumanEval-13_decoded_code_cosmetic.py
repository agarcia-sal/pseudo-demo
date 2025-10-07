from typing import Union

def greatest_common_divisor(operand_x: int, operand_y: int) -> int:
    while operand_y != 0:
        placeholder_var = operand_y
        operand_y = operand_x - (operand_x // operand_y) * operand_y
        operand_x = placeholder_var
    return operand_x