from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    locs: List[Tuple[int, int]] = []
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            element = row[j]
            if element == key:
                locs.append((i, j))

    # Sort by column index descending
    locs_sorted_by_second_desc = sorted(locs, key=lambda x: x[1], reverse=True)
    # Then stable sort by row index ascending
    locs_sorted_by_first_asc = sorted(locs_sorted_by_second_desc, key=lambda x: x[0])
    return locs_sorted_by_first_asc