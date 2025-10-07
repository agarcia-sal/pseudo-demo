class Solution:
    def maxScore(self, grid):
        # Sort each row in descending order
        for i in range(len(grid)):
            temp_row = grid[i][:]
            sorted_temp = []
            while temp_row:
                max_val = temp_row[0]
                max_idx = 0
                for idx in range(1, len(temp_row)):
                    compare_val = temp_row[idx]
                    if compare_val > max_val:
                        max_val = compare_val
                        max_idx = idx
                sorted_temp.append(max_val)
                temp_row = temp_row[:max_idx] + temp_row[max_idx+1:]
            grid[i] = sorted_temp

        max_sum = 0

        def backtrack(lambda1, lambda2, lambda3):
            nonlocal max_sum
            if lambda1 == len(grid):
                if lambda3 > max_sum:
                    max_sum = lambda3
                return
            backtrack(lambda1 + 1, lambda2, lambda3)
            for element_var in grid[lambda1]:
                if element_var not in lambda2:
                    lambda2.add(element_var)
                    backtrack(lambda1 + 1, lambda2, lambda3 + element_var)
                    lambda2.remove(element_var)

        backtrack(0, set(), 0)
        return max_sum