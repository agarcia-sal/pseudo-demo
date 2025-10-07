from typing import List, Tuple

def get_row(matrix: List[List[int]], value: int) -> List[Tuple[int, int]]:
    def collect_coords(i: int, j: int, acc: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if i == len(matrix):
            return acc
        elif j == len(matrix[i]):
            return collect_coords(i + 1, 0, acc)
        else:
            new_acc = acc + [(i, j)] if matrix[i][j] == value else acc
            return collect_coords(i, j + 1, new_acc)

    gathered = collect_coords(0, 0, [])

    def sort_by_row_then_col(lst: List[Tuple[int, int]], index1: int, index2: int) -> List[Tuple[int, int]]:
        def comparator(a: Tuple[int, int], b: Tuple[int, int]) -> int:
            if a[index1] < b[index1]:
                return -1
            if a[index1] > b[index1]:
                return 1
            if a[index2] > b[index2]:
                return -1
            if a[index2] < b[index2]:
                return 1
            return 0

        return sorted(lst, key=lambda x: (x[index1], -x[index2]))

    return sort_by_row_then_col(gathered, 0, 1)