from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coords: List[Tuple[int, int]] = []
    i = 0
    while i < len(lst):
        row = lst[i]
        j = 0
        while j < len(row):
            if row[j] == x:
                coords.append((i, j))
            j += 1
        i += 1
    coords_sorted_by_column_desc: List[Tuple[int, int]] = []
    temp_list = coords.copy()
    while len(temp_list) > 0:
        max_item = temp_list[0]
        index_to_remove = 0
        k = 1
        while k < len(temp_list):
            if temp_list[k][1] > max_item[1]:
                max_item = temp_list[k]
                index_to_remove = k
            k += 1
        coords_sorted_by_column_desc.append(max_item)
        temp_list.pop(index_to_remove)
    coords_sorted_by_row_asc: List[Tuple[int, int]] = []
    temp_list2 = coords_sorted_by_column_desc.copy()
    while len(temp_list2) > 0:
        min_item = temp_list2[0]
        index_to_remove2 = 0
        m = 1
        while m < len(temp_list2):
            if temp_list2[m][0] < min_item[0]:
                min_item = temp_list2[m]
                index_to_remove2 = m
            m += 1
        coords_sorted_by_row_asc.append(min_item)
        temp_list2.pop(index_to_remove2)
    return coords_sorted_by_row_asc