class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0

        sizeM = len(grid)
        sizeN = len(grid[0])

        prefix_sum = [[0] * sizeN for _ in range(sizeM)]

        tally = 0
        for outerIdx in range(sizeM):
            for innerIdx in range(sizeN):
                if outerIdx == 0 and innerIdx == 0:
                    prefix_sum[outerIdx][innerIdx] = grid[outerIdx][innerIdx]
                elif outerIdx == 0:
                    prefix_sum[outerIdx][innerIdx] = prefix_sum[outerIdx][innerIdx - 1] + grid[outerIdx][innerIdx]
                elif innerIdx == 0:
                    prefix_sum[outerIdx][innerIdx] = prefix_sum[outerIdx - 1][innerIdx] + grid[outerIdx][innerIdx]
                else:
                    prefix_sum[outerIdx][innerIdx] = (prefix_sum[outerIdx][innerIdx - 1]
                                                     + prefix_sum[outerIdx - 1][innerIdx]
                                                     - prefix_sum[outerIdx - 1][innerIdx - 1]
                                                     + grid[outerIdx][innerIdx])
                if prefix_sum[outerIdx][innerIdx] <= k:
                    tally += 1

        return tally