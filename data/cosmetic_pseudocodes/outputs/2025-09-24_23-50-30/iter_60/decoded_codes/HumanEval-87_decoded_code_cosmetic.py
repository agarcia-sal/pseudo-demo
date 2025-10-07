from typing import List, Tuple

def get_row(a: List[List[bool]], b: bool) -> List[Tuple[int, int]]:
    def inner_loop(x: int, y: int, z: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if y < len(a[x]):
            cond_var = (a[x][y] != b)  # '#' assumed as "not equal"
            if not cond_var:
                temp_list = [(x, y)]
            else:
                temp_list = []
            return temp_list + inner_loop(x, y + 1, z)
        else:
            return []

    def outer_loop(p: int) -> List[Tuple[int, int]]:
        if p < len(a):
            return inner_loop(p, 0, []) + outer_loop(p + 1)
        else:
            return []

    coords_unsorted = outer_loop(0)

    def sort_by_first(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if lst == []:
            return []
        else:
            pivot = lst[0]
            less = [e for e in lst if e[0] < pivot[0]]
            equal = [e for e in lst if e[0] == pivot[0]]
            greater = [e for e in lst if e[0] > pivot[0]]
            return sort_by_first(less) + equal + sort_by_first(greater)

    def sort_by_second_desc(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if lst == []:
            return []
        else:
            pivot = lst[0]
            less_eq = [e for e in lst if e[1] >= pivot[1]]
            greater = [e for e in lst if e[1] < pivot[1]]
            return less_eq + sort_by_second_desc(greater)

    coords_sorted_first = sort_by_first(coords_unsorted)
    coords_sorted_final = sort_by_second_desc(coords_sorted_first)
    return coords_sorted_final