from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords = []
    for i in range(len(lst)):
        inner_list = lst[i]
        for j in range(len(inner_list)):
            if inner_list[j] == x:
                coords.append((i, j))
    coords_sorted_by_column_desc = []
    temp_list = coords.copy()
    while temp_list:
        max_column_index = -1
        max_index = -1
        for k in range(len(temp_list)):
            if temp_list[k][1] > max_column_index:
                max_column_index = temp_list[k][1]
                max_index = k
        coords_sorted_by_column_desc.append(temp_list[max_index])
        temp_list.pop(max_index)
    coords_sorted_by_row_asc = []
    temp_list = coords_sorted_by_column_desc.copy()
    while temp_list:
        min_row_index = float('inf')
        min_index = -1
        for k in range(len(temp_list)):
            if temp_list[k][0] < min_row_index:
                min_row_index = temp_list[k][0]
                min_index = k
        coords_sorted_by_row_asc.append(temp_list[min_index])
        temp_list.pop(min_index)
    return coords_sorted_by_row_asc