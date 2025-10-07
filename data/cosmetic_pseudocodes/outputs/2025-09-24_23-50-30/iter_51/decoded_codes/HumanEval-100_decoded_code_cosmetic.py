from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    def build_values(current: int, acc: List[int]) -> List[int]:
        if current >= positive_integer_n:
            return acc
        else:
            return build_values(current + 1, acc + [(2 * current) + positive_integer_n])
    return build_values(0, [])