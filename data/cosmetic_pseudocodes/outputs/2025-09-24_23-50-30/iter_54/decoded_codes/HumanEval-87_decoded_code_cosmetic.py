from typing import List, Tuple


def get_row(two_dimensional_list: List[List[int]], target_integer: int) -> List[Tuple[int, int]]:
    def explore_rows(current_row: int, acc_coordinates: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if current_row >= len(two_dimensional_list):
            return acc_coordinates

        def explore_columns(current_col: int, row_accum: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if current_col >= len(two_dimensional_list[current_row]):
                return row_accum
            if two_dimensional_list[current_row][current_col] == target_integer:
                return explore_columns(current_col + 1, row_accum + [(current_row, current_col)])
            else:
                return explore_columns(current_col + 1, row_accum)

        updated_acc = explore_columns(0, acc_coordinates)
        return explore_rows(current_row + 1, updated_acc)

    all_coordinates = explore_rows(0, [])

    sorted_by_second_desc: List[Tuple[int, int]] = []
    for coord in all_coordinates:
        inserted = False
        for i in range(len(sorted_by_second_desc)):
            if sorted_by_second_desc[i][1] < coord[1]:
                sorted_by_second_desc.insert(i, coord)
                inserted = True
                break
        if not inserted:
            sorted_by_second_desc.append(coord)

    final_sorted: List[Tuple[int, int]] = []
    for coord in sorted_by_second_desc:
        placed = False
        for j in range(len(final_sorted)):
            if final_sorted[j][0] > coord[0]:
                final_sorted.insert(j, coord)
                placed = True
                break
        if not placed:
            final_sorted.append(coord)

    return final_sorted