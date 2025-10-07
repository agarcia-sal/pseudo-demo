class Solution:
    def maxScore(self, grid):
        total_maximum = 0

        def backtrack(current_row, visited_elements, aggregate_sum):
            nonlocal total_maximum
            if current_row >= len(grid):
                if aggregate_sum > total_maximum:
                    total_maximum = aggregate_sum
                return
            # option to skip current row
            backtrack(current_row + 1, visited_elements, aggregate_sum)
            for element_value in grid[current_row]:
                if element_value not in visited_elements:
                    visited_elements.add(element_value)
                    backtrack(current_row + 1, visited_elements, aggregate_sum + element_value)
                    visited_elements.remove(element_value)

        for row in grid:
            # sort rows descending using Python built-in sort for clarity and efficiency
            row.sort(reverse=True)

        backtrack(0, set(), 0)
        return total_maximum