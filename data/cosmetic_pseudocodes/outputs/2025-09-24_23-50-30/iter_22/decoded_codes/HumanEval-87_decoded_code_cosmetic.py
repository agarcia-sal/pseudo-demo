from typing import List, Tuple, Set

def get_row(matrix: List[List[int]], key: int) -> List[Tuple[int, int]]:
    def collect_positions(acc: Set[Tuple[int, int]], r: int) -> Set[Tuple[int, int]]:
        if r >= len(matrix):
            return acc
        row = matrix[r]
        def collect_cols(c: int, temp: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            if c >= len(row):
                return temp
            if row[c] == key:
                return collect_cols(c + 1, temp | {(r, c)})
            return collect_cols(c + 1, temp)
        return collect_positions(acc | collect_cols(0, set()), r + 1)

    pos = collect_positions(set(), 0)
    sorted_by_col_desc = sorted(pos, key=lambda x: x[1], reverse=True)
    final_sorted = sorted(sorted_by_col_desc, key=lambda x: x[0])
    return final_sorted