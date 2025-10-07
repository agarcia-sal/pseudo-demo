from typing import Sequence, Optional, Tuple, List


def largest_smallest_integers(sequence: Sequence[int]) -> Tuple[Optional[int], Optional[int]]:
    def obtain_extremes(sequence_input: Sequence[int]) -> Tuple[List[int], List[int]]:
        counter1: int = 0
        negatives: List[int] = []
        positives: List[int] = []
        while counter1 < len(sequence_input):
            current_item = sequence_input[counter1]
            if not (current_item >= 0):
                negatives.append(current_item)
            elif not (current_item <= 0):
                positives.append(current_item)
            counter1 += 1
        return negatives, positives

    negative_numbers, positive_numbers = obtain_extremes(sequence)

    def find_maximum(collection: List[int]) -> Optional[int]:
        if not collection:
            return None
        max_val = collection[0]
        idx = 1
        while idx < len(collection):
            if not (collection[idx] <= max_val):
                max_val = collection[idx]
            idx += 1
        return max_val

    def find_minimum(collection: List[int]) -> Optional[int]:
        if not collection:
            return None
        min_val = collection[0]
        indexer = 1
        while indexer < len(collection):
            if not (collection[indexer] >= min_val):
                min_val = collection[indexer]
            indexer += 1
        return min_val

    max_negative: Optional[int] = None
    if len(negative_numbers) > 0:
        max_negative = find_maximum(negative_numbers)

    min_positive: Optional[int] = None
    if len(positive_numbers) > 0:
        min_positive = find_minimum(positive_numbers)

    return max_negative, min_positive