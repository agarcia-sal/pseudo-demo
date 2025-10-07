from typing import List, Tuple

def get_row(matrix: List[List[int]], key: int) -> List[Tuple[int, int]]:
    def collect_positions(row_pos: int, col_pos: int, accum: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if row_pos >= len(matrix):
            return accum
        else:
            def process_cols(col_pos_inner: int, accum_inner: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if col_pos_inner >= len(matrix[row_pos]):
                    return accum_inner
                else:
                    accum_updated = (
                        accum_inner + [(row_pos, col_pos_inner)]
                        if matrix[row_pos][col_pos_inner] == key
                        else accum_inner
                    )
                    return process_cols(col_pos_inner + 1, accum_updated)
            accum_after_cols = process_cols(0, accum)
            return collect_positions(row_pos + 1, col_pos, accum_after_cols)

    collected_coords = collect_positions(0, 0, [])
    ordered_coords_desc = sorted(collected_coords, key=lambda x: x[1], reverse=True)
    ordered_coords = sorted(ordered_coords_desc, key=lambda x: x[0])
    return ordered_coords