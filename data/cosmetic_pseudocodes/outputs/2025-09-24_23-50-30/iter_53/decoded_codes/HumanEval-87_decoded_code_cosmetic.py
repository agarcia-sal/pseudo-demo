from typing import List, Tuple, Callable

def get_row(uniform_structure: List[List[int]], pivotal_value: int) -> List[Tuple[int, int]]:
    def explore_positions(
        position_tracker: List[Tuple[int, int]],
        current_primary: int,
        boundary_primary: int,
        primary_limit: int
    ) -> List[Tuple[int, int]]:
        if current_primary > boundary_primary:
            return position_tracker
        else:
            def traverse_secondary(
                positions_list: List[Tuple[int, int]],
                current_secondary: int,
                boundary_secondary: int
            ) -> List[Tuple[int, int]]:
                if current_secondary > boundary_secondary:
                    return positions_list
                else:
                    if uniform_structure[current_primary][current_secondary] == pivotal_value:
                        positions_list.append((current_primary, current_secondary))
                    return traverse_secondary(positions_list, current_secondary + 1, boundary_secondary)

            updated_positions = traverse_secondary(
                position_tracker,
                0,
                len(uniform_structure[current_primary]) - 1
            )
            return explore_positions(updated_positions, current_primary + 1, boundary_primary, primary_limit)

    interim_coords: List[Tuple[int, int]] = explore_positions([], 0, len(uniform_structure) - 1, len(uniform_structure))

    def insertion_sort(
        coords_list: List[Tuple[int, int]],
        index: int,
        n: int,
        comparator: Callable[[Tuple[int, int], Tuple[int, int]], bool]
    ) -> List[Tuple[int, int]]:
        if index >= n:
            return coords_list
        key_element = coords_list[index]
        predecessor = index - 1
        while predecessor >= 0 and comparator(coords_list[predecessor], key_element):
            coords_list[predecessor + 1] = coords_list[predecessor]
            predecessor -= 1
        coords_list[predecessor + 1] = key_element
        return insertion_sort(coords_list, index + 1, n, comparator)

    def sort_by_second_desc(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return a[1] < b[1]

    def sort_by_first_asc(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
        return a[0] > b[0]

    after_second_sort = insertion_sort(interim_coords, 1, len(interim_coords), sort_by_second_desc)
    after_first_sort = insertion_sort(after_second_sort, 1, len(after_second_sort), sort_by_first_asc)

    return after_first_sort