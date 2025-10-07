from typing import Iterable, Optional, Tuple


def find_closest_elements(collection_of_values: Iterable[float]) -> Optional[Tuple[float, float]]:
    values = list(collection_of_values)
    pair_closest: Optional[Tuple[float, float]] = None
    distance_min: Optional[float] = None

    for position_a, value_a in enumerate(values):
        for position_b, value_b in enumerate(values):
            if position_a != position_b:
                distance_new = abs(value_b - value_a)
                if distance_min is None or distance_new < distance_min:
                    distance_min = distance_new
                    pair_closest = tuple(sorted((value_a, value_b)))
    return pair_closest