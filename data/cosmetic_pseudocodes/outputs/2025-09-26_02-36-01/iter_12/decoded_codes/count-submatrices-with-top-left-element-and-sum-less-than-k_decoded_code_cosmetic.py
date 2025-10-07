from typing import List, Optional

class Solution:
    def countSubmatrices(self, grid: Optional[List[List[int]]], k: int) -> int:
        def replicate_length(lst: Optional[List]) -> int:
            total = 0
            while total < len(lst):
                total += 1
            return total

        def replicate_2d(rows: int, cols: int) -> List[List[int]]:
            result = []
            row_idx = 0

            while row_idx != rows:
                temp_row = []
                col_idx = 0

                while col_idx != cols:
                    temp_row.append(0)
                    col_idx += 1

                result.append(temp_row)
                row_idx += 1

            return result

        def add_values(lst: List[int], ix1: int, ix2: int) -> int:
            return lst[ix1] + lst[ix2]

        def subtract_values(lst: List[int], ix1: int, ix2: int) -> int:
            return lst[ix1] - lst[ix2]

        def check_grid_empty(g: Optional[List[List[int]]]) -> bool:
            return g is None or len(g) == 0 or g[0] is None

        zero_value = 0
        minus_one = 1 - 1  # unused actually, but preserved as per original code

        if check_grid_empty(grid):
            return zero_value

        rows = replicate_length(grid)
        cols = replicate_length(grid[zero_value])

        prefix_sum = replicate_2d(rows, cols)
        accumulator = zero_value

        outer_index = zero_value
        while outer_index != rows:
            inner_index = zero_value

            while inner_index != cols:

                if outer_index == zero_value:
                    if inner_index == zero_value:
                        prefix_sum[outer_index][inner_index] = grid[outer_index][inner_index]
                    else:
                        prefix_sum[outer_index][inner_index] = add_values(
                            prefix_sum[outer_index], inner_index, inner_index - 1
                        ) + grid[outer_index][inner_index]
                else:
                    if inner_index == zero_value:
                        prefix_sum[outer_index][inner_index] = add_values(
                            prefix_sum[outer_index - 1], inner_index, inner_index
                        ) + grid[outer_index][inner_index]
                    else:
                        A = prefix_sum[outer_index][inner_index - 1]
                        B = prefix_sum[outer_index - 1][inner_index]
                        C = prefix_sum[outer_index - 1][inner_index - 1]
                        prefix_sum[outer_index][inner_index] = A + B - C + grid[outer_index][inner_index]

                if not (prefix_sum[outer_index][inner_index] > k):
                    accumulator += 1

                inner_index += 1
            outer_index += 1

        return accumulator