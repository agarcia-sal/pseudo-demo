from typing import Callable, List, Optional, Tuple, Union, Sequence
import math

def largest_smallest_integers(collection_of_values: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    def locate_maximum(values_collection: Sequence[int], index: int) -> int:
        if index > len(values_collection):
            return -math.inf  # represents -∞
        candidate = values_collection[index - 1]
        next_max = locate_maximum(values_collection, index + 1)
        return candidate if candidate > next_max else next_max

    def locate_minimum(values_collection: Sequence[int], position: int) -> int:
        if position > len(values_collection):
            return math.inf  # represents +∞
        contender = values_collection[position - 1]
        next_min = locate_minimum(values_collection, position + 1)
        return contender if contender < next_min else next_min

    def collect_filtered(
        predicate: Callable[[int], bool],
        source_list: Sequence[int],
        acc: List[int],
        current_index: int,
    ) -> List[int]:
        if current_index > len(source_list):
            return acc
        element = source_list[current_index - 1]
        if predicate(element):
            return collect_filtered(predicate, source_list, acc + [element], current_index + 1)
        else:
            return collect_filtered(predicate, source_list, acc, current_index + 1)

    negatives = collect_filtered(lambda value: value < 0, collection_of_values, [], 1)
    positives = collect_filtered(lambda value: value > 0, collection_of_values, [], 1)

    max_neg: Optional[int] = None if len(negatives) == 0 else locate_maximum(negatives, 1)
    min_pos: Optional[int] = None if len(positives) == 0 else locate_minimum(positives, 1)

    return (max_neg, min_pos)