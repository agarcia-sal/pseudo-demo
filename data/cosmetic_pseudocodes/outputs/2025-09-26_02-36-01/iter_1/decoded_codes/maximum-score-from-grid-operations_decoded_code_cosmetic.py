class Solution:
    def maximumScore(self, grid):
        size = len(grid)
        prefixSum = [[0] * (size + 1) for _ in range(size + 1)]
        lastPicked = [0] * (size + 1)
        lastSkipped = [0] * (size + 1)

        for col in range(size):
            for row in range(size):
                prefixSum[col][row + 1] = prefixSum[col][row] + grid[row][col]

        for idx in range(1, size):
            currentPicked = [0] * (size + 1)
            currentSkipped = [0] * (size + 1)

            for current in range(size + 1):
                for previous in range(size + 1):
                    if current > previous:
                        segmentScore = prefixSum[idx - 1][current] - prefixSum[idx - 1][previous]
                        currentPicked[current] = max(currentPicked[current], lastSkipped[previous] + segmentScore)
                        currentSkipped[current] = max(currentSkipped[current], lastSkipped[previous] + segmentScore)
                    else:
                        segmentScore = prefixSum[idx][previous] - prefixSum[idx][current]
                        currentPicked[current] = max(currentPicked[current], lastPicked[previous] + segmentScore)
                        currentSkipped[current] = max(currentSkipped[current], lastPicked[previous])

            lastPicked = currentPicked
            lastSkipped = currentSkipped

        return max(lastPicked)