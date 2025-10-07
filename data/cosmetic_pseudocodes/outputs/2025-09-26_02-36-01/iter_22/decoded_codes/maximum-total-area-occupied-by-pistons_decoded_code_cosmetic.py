class Solution:
    def maxArea(self, height, positions, directions):
        totalPositionsCount = sum(positions)
        maxAreaValue = totalPositionsCount

        directions = list(directions)  # Convert string to list for mutable operations
        for timeStep in range(1, height * 2 + 1):
            for posIndex in range(len(positions)):
                if positions[posIndex] == 0 and directions[posIndex] == 'D':
                    directions[posIndex] = 'U'
                elif positions[posIndex] == height and directions[posIndex] == 'U':
                    directions[posIndex] = 'D'

                if directions[posIndex] == 'U':
                    positions[posIndex] += 1
                else:
                    positions[posIndex] -= 1

            currentSum = sum(positions)
            if maxAreaValue < currentSum:
                maxAreaValue = currentSum

        return maxAreaValue