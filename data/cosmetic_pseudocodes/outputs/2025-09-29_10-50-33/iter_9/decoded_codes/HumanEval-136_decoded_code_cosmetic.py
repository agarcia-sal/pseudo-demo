from typing import List, Optional, Iterator, Tuple


def largest_smallest_integers(list_of_numbers: List[int]) -> Iterator[Tuple[Optional[int], Optional[int]]]:
    def recursive_filter_negatives(collection: List[int], position: int, accumulator: List[int]) -> List[int]:
        if position == len(collection):
            return accumulator
        if collection[position] < 0:
            return recursive_filter_negatives(collection, position + 1, accumulator + [collection[position]])
        return recursive_filter_negatives(collection, position + 1, accumulator)

    def recursive_filter_positives(collection: List[int], count: int, gather: List[int]) -> List[int]:
        if count == len(collection):
            return gather
        if collection[count] > 0:
            return recursive_filter_positives(collection, count + 1, gather + [collection[count]])
        return recursive_filter_positives(collection, count + 1, gather)

    def fold_maximum(numbers: List[int], idx: int, current_maximum: int) -> int:
        if idx >= len(numbers):
            return current_maximum
        next_max = numbers[idx] if numbers[idx] > current_maximum else current_maximum
        return fold_maximum(numbers, idx + 1, next_max)

    def fold_minimum(numbers: List[int], offset: int, current_minimum: int) -> int:
        if offset >= len(numbers):
            return current_minimum
        next_min = numbers[offset] if numbers[offset] < current_minimum else current_minimum
        return fold_minimum(numbers, offset + 1, next_min)

    negatives_filtered = recursive_filter_negatives(list_of_numbers, 0, [])
    positives_filtered = recursive_filter_positives(list_of_numbers, 0, [])

    if len(negatives_filtered) == 0:
        max_neg_val: Optional[int] = None
    else:
        max_neg_val = fold_maximum(negatives_filtered, 0, negatives_filtered[0])

    if len(positives_filtered) != 0:
        min_pos_val = fold_minimum(positives_filtered, 0, positives_filtered[0])
    else:
        min_pos_val = None

    yield (max_neg_val, min_pos_val)