class Solution:
    def maxScore(self, grid):
        max_sum = 0

        def exploreLevel(depth, tracked, accumulator):
            nonlocal max_sum
            if depth >= len(grid):
                if accumulator > max_sum:
                    max_sum = accumulator
                return
            exploreLevel(depth + 1, tracked, accumulator)
            for candidate in grid[depth]:
                if candidate not in tracked:
                    tracked.add(candidate)
                    exploreLevel(depth + 1, tracked, accumulator + candidate)
                    tracked.remove(candidate)

        # Sort each row of grid in descending order using bubble sort as per pseudocode
        indexVar = 0
        while indexVar < len(grid):
            a = grid[indexVar]
            i = 0
            while i < len(a) - 1:
                j = 0
                while j < len(a) - i - 1:
                    if a[j] < a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
                    j += 1
                i += 1
            indexVar += 1

        exploreLevel(0, set(), 0)
        return max_sum