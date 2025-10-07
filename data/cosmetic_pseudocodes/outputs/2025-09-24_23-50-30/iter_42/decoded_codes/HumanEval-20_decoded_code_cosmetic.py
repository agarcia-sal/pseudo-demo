from typing import Sequence, Optional, Tuple


def find_closest_elements(input_sequence: Sequence[int]) -> Optional[Tuple[int, int]]:
    minimal_gap: Optional[int] = None
    adjacent_elements: Optional[Tuple[int, int]] = None

    for index_outer, element_outer in enumerate(input_sequence):
        for index_inner, element_inner in enumerate(input_sequence):
            if index_inner != index_outer:
                computed_gap = abs(element_outer - element_inner)
                if minimal_gap is None or computed_gap < minimal_gap:
                    minimal_gap = computed_gap
                    # Store elements ordered ascending
                    adjacent_elements = (element_outer, element_inner) if element_outer <= element_inner else (element_inner, element_outer)

    return adjacent_elements