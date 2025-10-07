from typing import List, Tuple, Dict

def get_row(matrix: List[List[int]], key: int) -> List[Tuple[int, int]]:
    def scan_rows(i: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if i >= len(matrix):
            return acc
        else:
            def scan_columns(j: int, inner_acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
                if j >= len(matrix[i]):
                    return inner_acc
                else:
                    updated_acc = inner_acc + [(i, j)] if matrix[i][j] == key else inner_acc
                    return scan_columns(j + 1, updated_acc)
            partial = scan_columns(0, acc)
            return scan_rows(i + 1, partial)

    collected = scan_rows(0, [])
    grouped: Dict[int, List[int]] = {}
    for r, c in collected:
        if r not in grouped:
            grouped[r] = []
        grouped[r].append(c)

    result: List[Tuple[int, int]] = []

    def insert_desc(lst: List[int], val: int) -> List[int]:
        if not lst or val >= lst[0]:
            return [val] + lst
        else:
            return [lst[0]] + insert_desc(lst[1:], val)

    for row_key in sorted(grouped.keys()):
        sorted_cols = grouped[row_key]
        sorted_rev_cols: List[int] = []
        for col_val in sorted_cols:
            sorted_rev_cols = insert_desc(sorted_rev_cols, col_val)
        for col_val in sorted_rev_cols:
            result.append((row_key, col_val))

    return result