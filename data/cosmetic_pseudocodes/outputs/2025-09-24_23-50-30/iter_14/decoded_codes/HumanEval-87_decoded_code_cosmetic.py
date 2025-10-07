from typing import List, Tuple, Any

def get_row(matrix: List[List[Any]], value: Any) -> List[Tuple[int, int]]:
    result: List[Tuple[int, int]] = []
    i: int = 0
    while i < len(matrix):
        j: int = 0
        while j < len(matrix[i]):
            # Equivalent to: if matrix[i][j] == value
            if not matrix[i][j] != value:
                result.append((i, j))
            j += 1
        i += 1
    # Sort by column descending (x[1] descending)
    sorted_by_col_desc = sorted(result, key=lambda x: x[1], reverse=True)
    # Then sort by row ascending (x[0] ascending), stable sort preserves column order inside equal rows
    sorted_by_row_asc = sorted(sorted_by_col_desc, key=lambda x: x[0])
    return sorted_by_row_asc