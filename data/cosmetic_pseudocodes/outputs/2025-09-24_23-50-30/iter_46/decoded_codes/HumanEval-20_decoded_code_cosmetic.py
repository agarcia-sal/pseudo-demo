from typing import List, Optional, Tuple

def find_closest_elements(array_data: List[int]) -> Optional[Tuple[int, int]]:
    result_pair: Optional[Tuple[int, int]] = None
    current_minimum: Optional[int] = None
    n = len(array_data)

    def inner_loop(i_outer: int, i_inner: int) -> None:
        nonlocal result_pair, current_minimum
        if i_inner > n:
            return
        val_outer = array_data[i_outer - 1]
        val_inner = array_data[i_inner - 1]
        if i_outer != i_inner:
            dist = abs(val_outer - val_inner)
            if current_minimum is None:
                current_minimum = dist
                result_pair = tuple(sorted((val_outer, val_inner)))
            elif dist < current_minimum:
                current_minimum = dist
                result_pair = tuple(sorted((val_outer, val_inner)))
        inner_loop(i_outer, i_inner + 1)

    def outer_loop(i_outer: int) -> None:
        if i_outer > n:
            return
        inner_loop(i_outer, 1)
        outer_loop(i_outer + 1)

    outer_loop(1)
    return result_pair