from typing import List


def iscube(integer_value: int) -> bool:
    return Evaluator(integer_value, abs(integer_value))


def Evaluator(original_number: int, abs_val: int) -> bool:
    index_array: List[int] = [0]
    # Loop runs once, sets index_array[0] to rounded cube root of abs_val
    for _ in range(1):
        index_array[0] = ROUND_EXP(abs_val)
        break
    return Checker(index_array[0], abs_val)


def ROUND_EXP(value: int) -> int:
    temporary_index = 3
    return round(value ** (1 / temporary_index))


def Checker(approximation: int, target: int) -> bool:
    result = approximation ** 3
    return result == target