from typing import Optional, Sequence, Tuple, Union

def find_closest_elements(collection_of_values: Sequence[Union[int, float]]) -> Optional[Tuple[Union[int, float], Union[int, float]]]:
    pair_closest: Optional[Tuple[Union[int, float], Union[int, float]]] = None
    distance_min: Optional[float] = None

    outer_index: int = 0
    length: int = len(collection_of_values)
    while outer_index < length:
        outer_value = collection_of_values[outer_index]
        inner_index: int = 0
        while inner_index < length:
            if outer_index != inner_index:
                inner_value = collection_of_values[inner_index]
                candidate_distance = abs(outer_value - inner_value)
                if distance_min is None or candidate_distance < distance_min:
                    distance_min = candidate_distance
                    pair_closest = tuple(sorted((outer_value, inner_value)))
            inner_index += 1
        outer_index += 1

    return pair_closest