from typing import List, Tuple, Any


def get_row(matrix: List[List[Any]], key: Any) -> List[Tuple[int, int]]:
    collector: List[Tuple[int, int]] = []

    def scan_cols(row_num: int, limit: int) -> None:
        if row_num >= limit:
            return

        def scan_cells(col_num: int, row: List[Any]) -> None:
            if col_num >= len(row):
                return
            if row[col_num] == key:
                collector.append((row_num, col_num))
            scan_cells(col_num + 1, row)

        scan_cells(0, matrix[row_num])
        scan_cols(row_num + 1, limit)

    scan_cols(0, len(matrix))

    # Sort by row ascending, then column descending
    collector.sort(key=lambda x: (x[0], -x[1]))

    return collector