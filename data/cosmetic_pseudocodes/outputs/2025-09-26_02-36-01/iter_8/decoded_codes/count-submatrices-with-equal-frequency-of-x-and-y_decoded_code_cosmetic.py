class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        rowLimit = len(grid)
        colLimit = len(grid[0])

        def helperInit():
            return [0, 0]

        # Initialize prefixMatrix with dimensions (rowLimit+1) x (colLimit+1) where each element is [0,0]
        prefixMatrix = [
            [helperInit() for _ in range(colLimit + 1)]
            for _ in range(rowLimit + 1)
        ]

        for indexA in range(1, rowLimit + 1):
            for indexB in range(1, colLimit + 1):
                tempX = (
                    prefixMatrix[indexA][indexB - 1][0] +
                    prefixMatrix[indexA - 1][indexB][0] -
                    prefixMatrix[indexA - 1][indexB - 1][0]
                )
                tempY = (
                    prefixMatrix[indexA][indexB - 1][1] +
                    prefixMatrix[indexA - 1][indexB][1] -
                    prefixMatrix[indexA - 1][indexB - 1][1]
                )

                cell = grid[indexA - 1][indexB - 1]
                if cell == 'X':
                    posX = tempX + 1
                    prefixMatrix[indexA][indexB][0] = posX
                    prefixMatrix[indexA][indexB][1] = tempY
                elif cell == 'Y':
                    posY = tempY + 1
                    prefixMatrix[indexA][indexB][1] = posY
                    prefixMatrix[indexA][indexB][0] = tempX
                else:
                    prefixMatrix[indexA][indexB][0] = tempX
                    prefixMatrix[indexA][indexB][1] = tempY

        totalCount = 0
        for accX in range(1, rowLimit + 1):
            for accY in range(1, colLimit + 1):
                tempX = prefixMatrix[accX][accY][0]
                tempY = prefixMatrix[accX][accY][1]
                if tempX > 0 and tempX == tempY:
                    totalCount += 1

        return totalCount