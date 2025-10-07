from typing import List

def string_sequence(integer_n: int) -> str:
    return ''.join(str(integer_x) for integer_x in range(integer_n + 1))