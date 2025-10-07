from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def recursive_sum(collection: List[int], idx: int, acc: int) -> int:
        if idx >= len(collection):
            return acc
        else:
            return recursive_sum(collection, idx + 1, acc + collection[idx])

    def inner_ceiling(value: float) -> int:
        if value == int(value):
            return int(value)
        else:
            return int(value) + 1

    def fold_over_rows(matrix: List[List[int]], indexer: int, accumulator: int) -> int:
        if indexer == len(matrix):
            return accumulator
        else:
            current_row_sum = recursive_sum(matrix[indexer], 0, 0)
            division_result = current_row_sum / capacity
            applied_ceiling = inner_ceiling(division_result)
            return fold_over_rows(matrix, indexer + 1, accumulator + applied_ceiling)

    return fold_over_rows(grid, 0, 0)