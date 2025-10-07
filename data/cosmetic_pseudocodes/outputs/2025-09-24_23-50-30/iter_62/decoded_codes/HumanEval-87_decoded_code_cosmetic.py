from typing import List, Tuple, Any

def get_row(data_structure: List[List[Any]], key_value: Any) -> List[Tuple[int, int]]:
    def recurse_row(i: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not (i < len(data_structure)):
            return acc
        else:
            return recurse_col(i, 0, acc)

    def recurse_col(row_idx: int, j: int, accum_list: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not (j < len(data_structure[row_idx])):
            return recurse_row(row_idx + 1, accum_list)
        else:
            if data_structure[row_idx][j] == key_value:
                new_accum_list = accum_list + [(row_idx, j)]
            else:
                new_accum_list = accum_list
            return recurse_col(row_idx, j + 1, new_accum_list)

    filtered_coords = recurse_row(0, [])

    def sort_by_first(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if lst == []:
            return []
        pivot = lst[0]
        less = [x for x in lst if x[0] < pivot[0]]
        equal = [x for x in lst if x[0] == pivot[0]]
        greater = [x for x in lst if x[0] > pivot[0]]
        return sort_by_first(less) + equal + sort_by_first(greater)

    def sort_by_second_desc(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if lst == []:
            return []
        pivot = lst[0]
        greater = [x for x in lst if x[1] > pivot[1]]
        equal = [x for x in lst if x[1] == pivot[1]]
        less = [x for x in lst if x[1] < pivot[1]]
        return greater + equal + sort_by_second_desc(less)

    step_one_sorted = sort_by_second_desc(filtered_coords)
    final_sorted = sort_by_first(step_one_sorted)

    return final_sorted