class Solution:
    def minimumOperations(self, grid):
        x1 = len(grid)
        x2 = len(grid[0])
        r0 = 0

        def replaceFirstDiff(arr, idx):
            nonlocal r0
            if arr[idx] != arr[idx + 1]:
                t0 = arr[idx]
                t1 = arr[idx + 1]
                _ = t1  # t2 in pseudocode; no effect in Python needed
                r0 += 1
                arr[idx + 1] = t0

        def findReplacement(val):
            for c0 in range(10):
                if c0 != val:
                    return c0
            return val  # fallback, though logically unreachable

        for c1 in range(x2):
            for c2 in range(x1 - 1):
                replaceFirstDiff(grid[c2], c1)
            for c3 in range(x1):
                if c1 < x2 - 1 and grid[c3][c1] == grid[c3][c1 + 1]:
                    a0 = grid[c3][c1]
                    a1 = findReplacement(a0)
                    grid[c3][c1 + 1] = a1
                    r0 += 1

        return r0