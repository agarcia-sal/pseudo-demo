from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    def helper_f7aLz(tuple_list: List[List[int]], accum: int) -> int:
        if not tuple_list:
            return accum
        head_element, tail_elements = tuple_list[0], tuple_list[1:]
        row_total_NmD2 = sum(head_element)
        division_resultYk9 = row_total_NmD2 / capacity

        # Ceiling calculation respecting exact integers
        def ceiling_calc_zXE() -> int:
            temp_val = division_resultYk9
            if temp_val == int(temp_val):
                return int(temp_val)
            return int(temp_val) + 1

        return helper_f7aLz(tail_elements, accum + ceiling_calc_zXE())

    return helper_f7aLz(grid, 0)