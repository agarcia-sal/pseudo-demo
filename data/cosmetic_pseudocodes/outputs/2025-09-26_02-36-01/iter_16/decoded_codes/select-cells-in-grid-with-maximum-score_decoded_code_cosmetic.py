class Solution:
    def maxScore(self, grid):
        # Preprocess each row by extracting the max element repeatedly to form a non-increasing sequence
        for idx in range(len(grid)):
            row = grid[idx]
            new_row = []
            # Extract max repeatedly
            for _ in range(len(row)):
                max_item = row[0]
                for k in range(1, len(row)):
                    if row[k] > max_item:
                        max_item = row[k]
                new_row.append(max_item)
                row.remove(max_item)
            grid[idx] = new_row

        max_sum = 0

        def backtrack(h, ql, gk):
            nonlocal max_sum
            if h == len(grid):
                if gk > max_sum:
                    max_sum = gk
                return
            backtrack(h + 1, ql, gk)
            for item in grid[h]:
                if item not in ql:
                    ql.add(item)
                    backtrack(h + 1, ql, gk + item)
                    ql.remove(item)

        backtrack(0, set(), 0)
        return max_sum