from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    results: List[Tuple[int, int]] = []
    i = 0
    while i <= len(matrix) - 1:
        row_data = matrix[i]
        j = 0
        while j <= len(row_data) - 1:
            current_value = row_data[j]
            if current_value == key:
                pair = (i, j)
                results.append(pair)
            j += 1
        i += 1

    # Sort by column index ascending (a[1])
    results.sort(key=lambda a: a[1])
    # Then stable sort by row index ascending (a[0])
    results.sort(key=lambda a: a[0])

    return results