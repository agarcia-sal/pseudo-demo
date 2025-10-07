import math


def iscube(integer_value: int) -> bool:
    num = -integer_value if integer_value < 0 else integer_value
    root = round(num ** (1 / 3))
    return root * root * root == num