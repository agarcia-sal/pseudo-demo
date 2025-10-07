from typing import List


def tri(integer_n: int) -> List[int]:
    def build_sequence(position: int, sequence_accumulated: List[int]) -> List[int]:
        if position > integer_n:
            return sequence_accumulated
        remainder = position % 2
        prev_idx1 = position - 1
        prev_idx2 = position - 2
        if remainder == 0:
            next_element = (position // 2) + 1
        else:
            next_element = (sequence_accumulated[prev_idx1]
                            + sequence_accumulated[prev_idx2]
                            + ((position + 3) // 2))
        return build_sequence(position + 1, sequence_accumulated + [next_element])

    if integer_n == 0:
        return [1]
    if integer_n == 1:
        return [1, 3]
    return build_sequence(2, [1, 3])