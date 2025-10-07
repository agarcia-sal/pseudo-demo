from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def fibonacci_style_counter(seq: List[int], idx: int, acc: int) -> int:
        if idx >= len(seq):
            return acc
        running_sum = acc + seq[idx]
        return fibonacci_style_counter(seq, idx + 1, running_sum)

    def ceiling_adder(accumulated: int, value: int) -> int:
        div_result = value / capacity
        int_division = int(div_result)
        has_fraction = div_result > int_division
        ceiling_result = int_division + (1 if has_fraction else 0)
        return accumulated + ceiling_result

    all_row_totals: List[int] = []
    for current_row in grid:
        row_total = fibonacci_style_counter(current_row, 0, 0)
        all_row_totals.append(row_total)

    total_accumulator = 0
    index_variable = 0
    while index_variable < len(all_row_totals):
        total_accumulator = ceiling_adder(total_accumulator, all_row_totals[index_variable])
        index_variable += 1

    return total_accumulator