from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    accumulator: List[int] = []

    def build_list(current_index: int) -> None:
        if current_index == positive_integer_n:
            return
        accumulator.append(positive_integer_n + current_index * 2)
        build_list(current_index + 1)

    build_list(0)
    return accumulator