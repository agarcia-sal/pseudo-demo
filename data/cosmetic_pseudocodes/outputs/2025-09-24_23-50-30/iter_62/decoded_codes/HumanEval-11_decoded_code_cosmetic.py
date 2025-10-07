from typing import Callable


def string_xor(input_one: str, input_two: str) -> str:
    def xor(inner_one: str, inner_two: str) -> str:
        return '0' if inner_one == inner_two else '1'

    def construct(index: int, accumulator: str) -> str:
        if index >= len(input_one) or index >= len(input_two):
            return accumulator
        return construct(index + 1, accumulator + xor(input_one[index], input_two[index]))

    return construct(0, "")