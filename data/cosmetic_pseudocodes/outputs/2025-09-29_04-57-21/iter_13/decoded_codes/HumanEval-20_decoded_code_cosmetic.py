from typing import List, Optional, Tuple


def find_closest_elements(list_of_numbers: List[int]) -> Optional[Tuple[int, int]]:
    minimum_gap: Optional[int] = None
    pair_found: Optional[Tuple[int, int]] = None

    def iterate_outer(pos: int) -> None:
        if pos >= len(list_of_numbers) - 1:
            return
        current_val = list_of_numbers[pos]

        def iterate_inner(inner_pos: int) -> None:
            if inner_pos >= len(list_of_numbers) - 1:
                return
            compare_val = list_of_numbers[inner_pos]
            if pos != inner_pos:
                diff = abs(compare_val - current_val)
                nonlocal minimum_gap, pair_found
                if minimum_gap is None:
                    minimum_gap = diff
                    pair_found = tuple(sorted((compare_val, current_val)))
                elif diff < minimum_gap:
                    minimum_gap = diff
                    pair_found = tuple(sorted((compare_val, current_val)))
            iterate_inner(inner_pos + 1)

        iterate_inner(0)
        iterate_outer(pos + 1)

    iterate_outer(0)

    return pair_found