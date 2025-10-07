from math import inf

class Solution:
    def maxScore(self, grid):
        max_sum = -inf
        length_grid = len(grid)

        def backtrack(current_row, used_values_set, total_score):
            nonlocal max_sum
            if current_row >= length_grid:
                if total_score > max_sum:
                    max_sum = total_score
                return

            # Option without selecting any candidate in the current row
            backtrack(current_row + 1, used_values_set, total_score)

            current_row_values = grid[current_row]
            count_values = len(current_row_values)
            index = 0
            while index < count_values:
                candidate = current_row_values[index]
                if candidate not in used_values_set:
                    used_values_set.add(candidate)
                    backtrack(current_row + 1, used_values_set, total_score + candidate)
                    used_values_set.remove(candidate)
                index += 1

        row_index = 0
        total_rows = len(grid)

        while row_index < total_rows:
            row_list = grid[row_index]
            sorted_list = []
            temp_index = 0
            while temp_index < len(row_list):
                sorted_list.append(row_list[temp_index])
                temp_index += 1

            def sort_descending(list_to_sort):
                n = len(list_to_sort)
                pass_num = 0
                while pass_num < n - 1:
                    i = 0
                    while i < n - pass_num - 1:
                        if list_to_sort[i] < list_to_sort[i + 1]:
                            temp_swap = list_to_sort[i]
                            list_to_sort[i] = list_to_sort[i + 1]
                            list_to_sort[i + 1] = temp_swap
                        i += 1
                    pass_num += 1

            sort_descending(sorted_list)
            grid[row_index] = sorted_list
            row_index += 1

        max_sum = 0
        backtrack(0, set(), 0)

        return max_sum