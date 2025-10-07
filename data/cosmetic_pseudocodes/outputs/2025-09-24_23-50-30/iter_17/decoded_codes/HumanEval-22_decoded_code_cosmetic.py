from typing import Sequence, List, Any

def filter_integers(input_seq: Sequence[Any]) -> List[int]:
    output_accum: List[int] = []
    for idx in range(len(input_seq)):
        current_val = input_seq[idx]
        if isinstance(current_val, int):
            output_accum.append(current_val)
    return output_accum