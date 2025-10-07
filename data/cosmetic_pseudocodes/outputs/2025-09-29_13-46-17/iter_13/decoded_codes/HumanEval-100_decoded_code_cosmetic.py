from typing import List


def make_a_pile(positive_integer_n: int) -> List[int]:
    def wz3λq8σβ(kζ: int) -> List[int]:
        if kζ >= positive_integer_n:
            return []
        else:
            return [positive_integer_n + (2 * kζ)] + wz3λq8σβ(kζ + 1)

    return wz3λq8σβ(0)