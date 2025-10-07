from typing import List, Tuple

def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def collect_matches(
        list_2d: List[List[int]],
        target_val: int,
        row_idx: int,
        col_idx: int,
        acc: List[Tuple[int, int]],
    ) -> List[Tuple[int, int]]:
        if row_idx >= len(list_2d):
            return acc
        if col_idx >= len(list_2d[row_idx]):
            return collect_matches(list_2d, target_val, row_idx + 1, 0, acc)
        if list_2d[row_idx][col_idx] == target_val:
            acc.append((row_idx, col_idx))
        return collect_matches(list_2d, target_val, row_idx, col_idx + 1, acc)

    found_coords = collect_matches(two_dimensional_list, target_integer, 0, 0, [])

    def custom_sort(list_coords: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if len(list_coords) <= 1:
            return list_coords
        pivot = list_coords[0]
        less_first: List[Tuple[int, int]] = []
        equal_first: List[Tuple[int, int]] = []
        greater_first: List[Tuple[int, int]] = []
        for item in list_coords:
            if item[0] < pivot[0]:
                less_first.append(item)
            elif item[0] == pivot[0]:
                equal_first.append(item)
            else:
                greater_first.append(item)

        sorted_less = custom_sort(less_first)
        sorted_greater = custom_sort(greater_first)

        def sort_by_second_desc(sublist: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(sublist) <= 1:
                return sublist
            p = sublist[0]
            lds: List[Tuple[int, int]] = []
            eds: List[Tuple[int, int]] = []
            gds: List[Tuple[int, int]] = []
            for el in sublist:
                if el[1] > p[1]:
                    lds.append(el)
                elif el[1] == p[1]:
                    eds.append(el)
                else:
                    gds.append(el)
            return sort_by_second_desc(lds) + eds + sort_by_second_desc(gds)

        sorted_equal_first = sort_by_second_desc(equal_first)
        return sorted_less + sorted_equal_first + sorted_greater

    return custom_sort(found_coords)