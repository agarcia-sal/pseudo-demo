from typing import List, Tuple

def rescale_to_unit(collection_of_values: List[float]) -> List[float]:
    def compute_range(current_min: float, current_max: float, remaining_values: List[float]) -> Tuple[float, float]:
        if not remaining_values:
            return current_min, current_max
        head_value, *tail_values = remaining_values
        new_min = head_value if head_value < current_min else current_min
        new_max = head_value if head_value > current_max else current_max
        return compute_range(new_min, new_max, tail_values)

    initial_value = collection_of_values[0]
    minimum_value, maximum_value = compute_range(initial_value, initial_value, collection_of_values[1:])
    denom = maximum_value - minimum_value

    def normalize_values(accumulator: List[float], remaining_values: List[float]) -> List[float]:
        if not remaining_values:
            return accumulator
        head_value, *tail_values = remaining_values
        normalized_value = (head_value - minimum_value) / denom
        return normalize_values(accumulator + [normalized_value], tail_values)

    return normalize_values([], collection_of_values)