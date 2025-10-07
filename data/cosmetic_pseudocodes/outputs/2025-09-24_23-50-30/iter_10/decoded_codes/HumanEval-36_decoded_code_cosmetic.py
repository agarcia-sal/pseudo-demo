from typing import List


def fizz_buzz(integer_n: int) -> int:
    accumulator: int = 0
    buffer: str = ""
    for integer_j in range(integer_n):
        if integer_j % 13 == 0 or integer_j % 11 == 0:
            buffer += str(integer_j)
    accumulator = sum(1 for character_x in buffer if character_x == '7')
    return accumulator