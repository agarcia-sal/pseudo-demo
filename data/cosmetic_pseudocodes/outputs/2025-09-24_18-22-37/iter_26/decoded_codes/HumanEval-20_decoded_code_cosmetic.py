from typing import Optional, Tuple, Sequence


def find_closest_elements(numbers_collection: Sequence[int]) -> Optional[Tuple[int, int]]:
    best_match: Optional[Tuple[int, int]] = None
    smallest_gap: Optional[int] = None

    outer_counter: int = 0
    length: int = len(numbers_collection)
    while outer_counter < length:
        outer_value: int = numbers_collection[outer_counter]

        inner_counter: int = 0
        while inner_counter < length:
            inner_value: int = numbers_collection[inner_counter]

            if outer_counter != inner_counter:
                distance_candidate: int = abs(outer_value - inner_value)
                if smallest_gap is None:
                    smallest_gap = distance_candidate
                    best_match = tuple(sorted((outer_value, inner_value)))
                elif distance_candidate < smallest_gap:
                    smallest_gap = distance_candidate
                    best_match = tuple(sorted((outer_value, inner_value)))
            inner_counter += 1

        outer_counter += 1

    return best_match