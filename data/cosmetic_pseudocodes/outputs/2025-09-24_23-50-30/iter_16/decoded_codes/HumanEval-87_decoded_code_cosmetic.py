from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    accumulator: List[Tuple[int, int]] = []

    def traverse_outer(index_outer: int) -> None:
        if index_outer >= len(two_dimensional_list):
            return
        current_inner_list = two_dimensional_list[index_outer]

        def traverse_inner(index_inner: int) -> None:
            if index_inner >= len(current_inner_list):
                return
            if not (current_inner_list[index_inner] != target_integer):
                accumulator.append((index_outer, index_inner))
            traverse_inner(index_inner + 1)

        traverse_inner(0)
        traverse_outer(index_outer + 1)

    traverse_outer(0)

    sorted_desc_by_second = sorted(accumulator, key=lambda element: -element[1])
    sorted_asc_by_first = sorted(sorted_desc_by_second, key=lambda element: element[0])

    return sorted_asc_by_first