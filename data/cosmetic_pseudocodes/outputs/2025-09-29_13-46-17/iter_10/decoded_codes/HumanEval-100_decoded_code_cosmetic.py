from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def build_pile(i: int) -> None:
        if i == positive_integer_n:
            return
        pile.append(i)
        build_pile(i + 1)

    pile: List[int] = []
    build_pile(0)
    return pile