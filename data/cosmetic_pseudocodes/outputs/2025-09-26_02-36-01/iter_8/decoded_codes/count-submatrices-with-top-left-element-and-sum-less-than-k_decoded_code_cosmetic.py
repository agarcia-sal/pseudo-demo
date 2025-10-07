class Solution:
    def countSubmatrices(self, grid, k):
        zeroVal = 0
        oneVal = 1
        twoVal = 2
        mLen = zeroVal
        nLen = zeroVal
        prefixSums = []
        totalCount = zeroVal

        if not (grid is not None and len(grid) > zeroVal and grid[zeroVal] is not None):
            return zeroVal

        mLen = len(grid)
        nLen = len(grid[zeroVal])

        rowIterator = zeroVal
        while rowIterator < mLen:
            newRow = []
            colFill = zeroVal
            while colFill < nLen:
                newRow.append(zeroVal)
                colFill += oneVal
            prefixSums.append(newRow)
            rowIterator += oneVal

        x = zeroVal
        while x < mLen:
            y = zeroVal
            while y < nLen:
                condA = (x == zeroVal)
                condB = (y == zeroVal)
                if condA and condB:
                    prefixSums[x][y] = grid[x][y]
                else:
                    if condA:
                        prefixSums[x][y] = prefixSums[x][y - oneVal] + grid[x][y]
                    else:
                        if condB:
                            prefixSums[x][y] = prefixSums[x - oneVal][y] + grid[x][y]
                        else:
                            tempSum = prefixSums[x][y - oneVal]
                            tempSum2 = prefixSums[x - oneVal][y]
                            tempSum3 = prefixSums[x - oneVal][y - oneVal]
                            prefixSums[x][y] = tempSum + tempSum2 - tempSum3 + grid[x][y]

                isWithinLimit = (prefixSums[x][y] <= k)
                if isWithinLimit:
                    totalCount += oneVal
                y += oneVal
            x += oneVal

        return totalCount