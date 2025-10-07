class Solution:
    def maxScore(self, grid):
        max_sum = 0

        def backtrack(idx, taken, total):
            nonlocal max_sum
            if idx == len(grid):
                if total > max_sum:
                    max_sum = total
                return
            backtrack(idx + 1, taken, total)
            for val in grid[idx]:
                if val not in taken:
                    taken.add(val)
                    backtrack(idx + 1, taken, total + val)
                    taken.remove(val)

        for row in grid:
            row.sort(reverse=True)

        backtrack(0, set(), 0)
        return max_sum