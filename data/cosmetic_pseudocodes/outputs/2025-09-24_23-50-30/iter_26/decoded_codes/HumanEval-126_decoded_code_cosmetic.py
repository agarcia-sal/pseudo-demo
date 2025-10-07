from typing import Sequence, TypeVar, Dict

T = TypeVar('T', bound=object)

def is_sorted(sequence: Sequence[T]) -> bool:
    frequency_map: Dict[T, int] = {element: 0 for element in sequence}

    def tally(index: int, freq_accum: Dict[T, int]) -> Dict[T, int]:
        if index == len(sequence):
            return freq_accum
        element = sequence[index]
        freq_accum[element] += 1
        return tally(index + 1, freq_accum)

    counted = tally(0, frequency_map)

    for key in sequence:
        if counted[key] > 2:
            return False

    def check_order(pos: int) -> bool:
        if pos == len(sequence) - 1:
            return True
        if sequence[pos - 1] <= sequence[pos]:
            return check_order(pos + 1)
        return False

    return check_order(1)