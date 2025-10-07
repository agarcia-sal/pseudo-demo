from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(sequence: Sequence[T]) -> float:
    temp_sequence = sorted(sequence)
    total = len(temp_sequence)

    if total % 2 != 0:
        return float(temp_sequence[(total - 1) // 2])

    mid1 = (total // 2) - 1
    mid2 = total // 2
    val1 = temp_sequence[mid1]
    val2 = temp_sequence[mid2]

    return (val1 + val2) / 2.0