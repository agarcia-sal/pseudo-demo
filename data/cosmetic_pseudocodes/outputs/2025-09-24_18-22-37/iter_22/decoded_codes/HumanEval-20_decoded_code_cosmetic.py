from typing import Optional, Tuple, Sequence, TypeVar

T = TypeVar('T', int, float)

def find_closest_elements(values_collection: Sequence[T]) -> Optional[Tuple[T, T]]:
    pair_closest: Optional[Tuple[T, T]] = None
    distance_minimal: Optional[T] = None

    length = len(values_collection)
    for idxA in range(length):
        valA = values_collection[idxA]

        for idxB in range(length):
            if idxA == idxB:
                continue
            valB = values_collection[idxB]

            diff_temp = valA - valB
            abs_temp = -diff_temp if diff_temp < 0 else diff_temp

            if distance_minimal is None or abs_temp < distance_minimal:
                distance_minimal = abs_temp
                pair_closest = (valA, valB) if valA < valB else (valB, valA)

    return pair_closest