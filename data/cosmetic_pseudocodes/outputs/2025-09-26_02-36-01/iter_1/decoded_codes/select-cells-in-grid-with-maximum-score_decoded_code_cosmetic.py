class Solution:
    def maxScore(self, grid):
        max_sum = 0
        for row in grid:
            row.sort(reverse=True)

        def backtrack(row, used, current_sum):
            nonlocal max_sum
            if row == len(grid):
                if current_sum > max_sum:
                    max_sum = current_sum
                return
            backtrack(row + 1, used, current_sum)
            for val in grid[row]:
                if val not in used:
                    used.add(val)
                    backtrack(row + 1, used, current_sum + val)
                    used.remove(val)

        backtrack(0, set(), 0)
        return max_sum