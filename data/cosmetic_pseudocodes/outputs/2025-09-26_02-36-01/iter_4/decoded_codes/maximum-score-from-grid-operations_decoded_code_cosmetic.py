class Solution:
    def maximumScore(self, grid):
        dimension_value = len(grid)
        accumulator = [[0] * (dimension_value + 1) for _ in range(dimension_value + 1)]
        earlier_selection = [0] * (dimension_value + 1)
        earlier_omission = [0] * (dimension_value + 1)

        for column_index in range(dimension_value):
            for row_index in range(dimension_value):
                accumulator[column_index][row_index + 1] = accumulator[column_index][row_index] + grid[row_index][column_index]

        for col_cursor in range(1, dimension_value):
            fresh_selection = [0] * (dimension_value + 1)
            fresh_omission = [0] * (dimension_value + 1)

            for current_pos in range(dimension_value + 1):
                for previous_pos in range(dimension_value + 1):
                    if current_pos > previous_pos:
                        segment_score = accumulator[col_cursor][current_pos - 1] - accumulator[col_cursor][previous_pos - 1]
                        candidate1 = fresh_selection[current_pos]
                        candidate2 = earlier_omission[previous_pos] + segment_score
                        if candidate1 < candidate2:
                            fresh_selection[current_pos] = candidate2

                        alt_candidate1 = fresh_omission[current_pos]
                        alt_candidate2 = earlier_omission[previous_pos] + segment_score
                        if alt_candidate1 < alt_candidate2:
                            fresh_omission[current_pos] = alt_candidate2
                    else:
                        segment_score = accumulator[col_cursor][previous_pos] - accumulator[col_cursor][current_pos]
                        candidate3 = fresh_selection[current_pos]
                        candidate4 = earlier_selection[previous_pos] + segment_score
                        if candidate3 < candidate4:
                            fresh_selection[current_pos] = candidate4

                        alt_candidate3 = fresh_omission[current_pos]
                        alt_candidate4 = earlier_selection[previous_pos]
                        if alt_candidate3 < alt_candidate4:
                            fresh_omission[current_pos] = alt_candidate4

            earlier_selection = fresh_selection
            earlier_omission = fresh_omission

        result_value = earlier_selection[0]
        for index_var in range(1, dimension_value + 1):
            if earlier_selection[index_var] > result_value:
                result_value = earlier_selection[index_var]

        return result_value