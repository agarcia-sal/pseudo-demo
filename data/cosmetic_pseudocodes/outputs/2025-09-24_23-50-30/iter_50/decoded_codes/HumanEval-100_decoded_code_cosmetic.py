from typing import List

def make_a_pile(positive_integer_n: int) -> List[int]:
    def build_sequence(current_pos: int, accumulator: List[int]) -> List[int]:
        if current_pos == positive_integer_n:
            return accumulator
        new_element = (2 * current_pos) + positive_integer_n
        return build_sequence(current_pos + 1, accumulator + [new_element])
    return build_sequence(0, [])