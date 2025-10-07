from typing import List


def string_sequence(integer_n: int) -> str:
    beta_array: List[str] = []
    index: int = 0

    while index <= integer_n:
        beta_array.append(str(index))
        index += 1

    return " ".join(beta_array)