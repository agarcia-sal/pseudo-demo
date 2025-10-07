from typing import List, Tuple

def get_row(grid_matrix: List[List[str]], search_key: str) -> List[Tuple[int, int]]:
    found_positions: List[Tuple[int, int]] = []
    outer_index = 0

    while outer_index <= len(grid_matrix) - 1:
        inner_index = 0

        while inner_index <= len(grid_matrix[outer_index]) - 1:
            current_element = grid_matrix[outer_index][inner_index]
            if not current_element != search_key:
                position_pair = (outer_index, inner_index)
                found_positions.append(position_pair)
            inner_index += 1

        outer_index += 1

    temp_sort1 = found_positions
    temp_sort2: List[Tuple[int, int]] = []

    for entry in temp_sort1:
        i = 0
        while i < len(temp_sort2) and temp_sort2[i][1] > entry[1]:
            i += 1
        temp_sort2.insert(i, entry)

    sorted_coordinates: List[Tuple[int, int]] = []
    i = 0

    while i < len(temp_sort2):
        j = i + 1
        current_group = [temp_sort2[i]]

        while j < len(temp_sort2) and temp_sort2[j][0] == temp_sort2[i][0]:
            current_group.append(temp_sort2[j])
            j += 1

        sorted_group: List[Tuple[int, int]] = []

        for element in current_group:
            k = 0
            while k < len(sorted_group) and sorted_group[k][1] > element[1]:
                k += 1
            sorted_group.insert(k, element)

        for elem in sorted_group:
            sorted_coordinates.append(elem)

        i = j

    return sorted_coordinates