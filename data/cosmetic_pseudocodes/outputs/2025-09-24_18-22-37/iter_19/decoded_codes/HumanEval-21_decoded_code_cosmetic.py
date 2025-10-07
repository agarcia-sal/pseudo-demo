from typing import List

def rescale_to_unit(list_of_numbers: List[float]) -> List[float]:
    alpha: float = 9999.0
    beta: float = -9999.0
    idx: int = 0
    length: int = len(list_of_numbers)

    while idx < length:
        val = list_of_numbers[idx]
        if val < alpha:
            alpha = val
        else:
            if val > beta:
                beta = val
        idx += 1

    delta = beta - alpha
    if delta == 0:
        # all values are equal; return zeros to avoid division by zero
        return [0.0] * length

    result: List[float] = []
    j: int = 0
    while True:
        if j >= length:
            break
        curr = list_of_numbers[j]
        scaled = (curr - alpha) / delta
        result.append(scaled)
        j += 1

    return result