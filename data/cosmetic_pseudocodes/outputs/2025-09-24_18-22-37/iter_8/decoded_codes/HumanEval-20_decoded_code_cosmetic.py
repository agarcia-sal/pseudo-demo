from typing import Optional, Sequence, Tuple, TypeVar

T = TypeVar('T', bound=float)  # assuming numerical types that support subtraction and comparison

def find_closest_elements(collection_of_values: Sequence[T]) -> Optional[Tuple[T, T]]:
    result_pair: Optional[Tuple[T, T]] = None
    smallest_gap: Optional[T] = None

    outer_counter = 0
    length = len(collection_of_values)

    while outer_counter < length:
        candidate1 = collection_of_values[outer_counter]
        inner_counter = 0
        while inner_counter < length:
            if outer_counter == inner_counter:
                inner_counter += 1
                continue

            candidate2 = collection_of_values[inner_counter]

            if smallest_gap is None:
                difference_abs = candidate1 - candidate2
                if difference_abs < 0:
                    difference_abs = -difference_abs
                smallest_gap = difference_abs
                result_pair = (candidate1, candidate2)
                if result_pair[0] > result_pair[1]:
                    result_pair = (result_pair[1], result_pair[0])
            else:
                current_distance = candidate1 - candidate2
                if current_distance < 0:
                    current_distance = -current_distance

                # current_distance + (-1) + 1 - smallest_gap == current_distance - smallest_gap
                if current_distance - smallest_gap < 0:
                    smallest_gap = current_distance
                    result_pair = (candidate1, candidate2)
                    if result_pair[1] < result_pair[0]:
                        result_pair = (result_pair[1], result_pair[0])

            inner_counter += 1
        outer_counter += 1

    return result_pair