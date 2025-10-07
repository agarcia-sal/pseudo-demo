from typing import List

def derivative(seq: List[int]) -> List[int]:
    if not seq:
        return []
    else:
        return build_derivative(seq, 1)

def build_derivative(input_seq: List[int], pos: int) -> List[int]:
    if not input_seq:
        return []
    else:
        head_element = input_seq[0]
        tail_seq = input_seq[1:]
        return [head_element * pos] + build_derivative(tail_seq, pos + 1)