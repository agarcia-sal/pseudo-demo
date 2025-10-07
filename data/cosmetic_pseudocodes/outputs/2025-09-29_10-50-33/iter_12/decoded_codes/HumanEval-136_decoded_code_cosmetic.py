from typing import Sequence, Optional, Tuple, List


def largest_smallest_integers(sequence_of_values: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    def find_maximum(values: Sequence[int]) -> Optional[int]:
        if values:
            index_tracker: int = 1
            current_peak: int = values[0]
            while index_tracker < len(values):
                if current_peak < values[index_tracker]:
                    current_peak = values[index_tracker]
                index_tracker += 1
            return current_peak
        return None

    def find_minimum(values: Sequence[int]) -> Optional[int]:
        if values:
            iterator_position: int = 0
            base_value: int = values[0]
            while iterator_position < len(values):
                if base_value > values[iterator_position]:
                    base_value = values[iterator_position]
                iterator_position += 1
            return base_value
        return None

    def filter_negatives(container: Sequence[int]) -> List[int]:
        pos: int = 0
        collection: List[int] = []
        while pos < len(container):
            if container[pos] < 0:
                collection.append(container[pos])
            pos += 1
        return collection

    def filter_positives(container: Sequence[int]) -> List[int]:
        idx: int = 0
        result_set: List[int] = []
        while idx < len(container):
            if not (container[idx] <= 0):
                result_set.append(container[idx])
            idx += 1
        return result_set

    negative_values: List[int] = filter_negatives(sequence_of_values)
    positive_values: List[int] = filter_positives(sequence_of_values)

    max_negative: Optional[int] = find_maximum(negative_values)
    min_positive: Optional[int] = find_minimum(positive_values)

    return max_negative, min_positive