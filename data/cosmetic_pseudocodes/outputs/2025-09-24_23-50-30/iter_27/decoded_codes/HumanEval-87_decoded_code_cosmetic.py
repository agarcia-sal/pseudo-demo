from typing import List, Tuple

def get_row(matrix_repr: List[List[int]], search_val: int) -> List[Tuple[int, int]]:
    position_records: List[Tuple[int, int]] = []
    idx_outer = 0
    while idx_outer < len(matrix_repr):
        idx_inner = 0
        while idx_inner < len(matrix_repr[idx_outer]):
            if matrix_repr[idx_outer][idx_inner] == search_val:
                position_records.append((idx_outer, idx_inner))
            idx_inner += 1
        idx_outer += 1
    # Sort by column descending, then by row ascending
    position_records.sort(key=lambda x: x[1], reverse=True)
    position_records.sort(key=lambda x: x[0])
    return position_records