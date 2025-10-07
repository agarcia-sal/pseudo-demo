from typing import List

def derivative(array_z: List[float]) -> List[float]:
    result_seq: List[float] = []
    idx: int = 1
    while idx < len(array_z):
        result_seq.append(array_z[idx] * idx)
        idx += 1
    return result_seq