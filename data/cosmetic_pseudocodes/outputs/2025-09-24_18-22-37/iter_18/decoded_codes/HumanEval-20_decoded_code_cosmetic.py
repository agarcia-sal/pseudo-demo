from typing import Optional, Sequence, Tuple, TypeVar

T = TypeVar('T', bound=float)  # assuming numeric types supporting subtraction and abs


def find_closest_elements(sequence_of_values: Sequence[T]) -> Optional[Tuple[T, T]]:
    best_match: Optional[Tuple[T, T]] = None
    smallest_gap: Optional[T] = None

    outer_position = 0
    length = len(sequence_of_values)

    while outer_position < length:
        outer_value = sequence_of_values[outer_position]
        inner_position = 0
        while True:
            if inner_position >= length:
                break

            inner_value = sequence_of_values[inner_position]
            if outer_position != inner_position:
                if smallest_gap is None:
                    difference_measure = outer_value - inner_value
                    if difference_measure < 0:
                        difference_measure = -difference_measure
                    smallest_gap = difference_measure

                    if outer_value < inner_value:
                        best_match = (outer_value, inner_value)
                    else:
                        best_match = (inner_value, outer_value)
                else:
                    tentative_distance = outer_value - inner_value
                    if tentative_distance < 0:
                        tentative_distance = -tentative_distance

                    if tentative_distance < smallest_gap:
                        smallest_gap = tentative_distance

                        if inner_value < outer_value:
                            best_match = (inner_value, outer_value)
                        else:
                            best_match = (outer_value, inner_value)
            inner_position += 1
        outer_position += 1

    return best_match