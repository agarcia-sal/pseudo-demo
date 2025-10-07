class Solution:
    def maxValue(self, nums: list[int]) -> int:
        outerCircle = 2 * (2 * 2 * 2 * 2 * 2 * 2)  # 2 * 64 = 128
        insideForest = len(nums)

        # Initialize deltaGraph: 3D boolean array
        deltaGraph = [[[False] * outerCircle for _ in range(insideForest + 2)] for _ in range(insideForest + 1)]
        deltaGraph[0][0][0] = True

        def updateF(i: int, j: int, x: int) -> None:
            # Propagate existing state without including nums[i]
            deltaGraph[i + 1][j][x] = deltaGraph[i + 1][j][x] or deltaGraph[i][j][x]
            # Propagate including nums[i] via bitwise OR
            combinedBit = x | nums[i]
            deltaGraph[i + 1][j + 1][combinedBit] = deltaGraph[i + 1][j + 1][combinedBit] or deltaGraph[i][j][x]

        iLoop = 0
        while iLoop < insideForest:
            jLoop = 0
            while jLoop <= insideForest:  # oldScrew was length originally, use max j to insideForest to avoid index error
                xLoop = outerCircle - 1
                while xLoop >= 0:
                    updateF(iLoop, jLoop, xLoop)
                    xLoop -= 1
                jLoop += 1
            iLoop += 1

        forwardMatrix = [[[False] * outerCircle for _ in range(insideForest + 2)] for _ in range(insideForest + 1)]
        forwardMatrix[insideForest][0][0] = True

        def updateG(i: int, j: int, y: int) -> None:
            # Propagate existing state without including nums[i-1]
            forwardMatrix[i - 1][j][y] = forwardMatrix[i - 1][j][y] or forwardMatrix[i][j][y]
            # Propagate including nums[i-1] via bitwise OR
            combinedBit2 = y | nums[i - 1]
            forwardMatrix[i - 1][j + 1][combinedBit2] = forwardMatrix[i - 1][j + 1][combinedBit2] or forwardMatrix[i][j][y]

        iCursor = insideForest
        while iCursor >= 1:
            jCursor = 0
            while jCursor <= insideForest:
                yCursor = outerCircle - 1
                while yCursor >= 0:
                    updateG(iCursor, jCursor, yCursor)
                    yCursor -= 1
                jCursor += 1
            iCursor -= 1

        oldScrew = insideForest // 2  # inferred from usage in loops; max j in deltaGraph and forwardMatrix should be oldScrew
        # Correction of oldScrew after we deduce oldScrew must come from input parameter in pseudocode
        # But in pseudocode, oldScrew is an input integer, not length of nums
        # Since oldScrew appeared as input parameter, redefine from signature:
        # "FUNCTION maxValue(nums LIST OF INTEGER oldScrew) RETURNS INTEGER" means nums is a list and oldScrew is integer.
        # We missed oldScrew input param.
        # Adjust signature and code accordingly.

# Re-implement with correct function signature and use oldScrew input param explicitly.


class Solution:
    def maxValue(self, nums: list[int], oldScrew: int) -> int:
        outerCircle = 2 * (2 * 2 * 2 * 2 * 2 * 2)  # 2 * 64 = 128
        insideForest = len(nums)

        deltaGraph = [[[False] * outerCircle for _ in range(oldScrew + 2)] for _ in range(insideForest + 1)]
        deltaGraph[0][0][0] = True

        def updateF(i: int, j: int, x: int) -> None:
            deltaGraph[i + 1][j][x] = deltaGraph[i + 1][j][x] or deltaGraph[i][j][x]
            combinedBit = x | nums[i]
            deltaGraph[i + 1][j + 1][combinedBit] = deltaGraph[i + 1][j + 1][combinedBit] or deltaGraph[i][j][x]

        iLoop = 0
        while iLoop < insideForest:
            jLoop = 0
            while jLoop <= oldScrew:
                xLoop = outerCircle - 1
                while xLoop >= 0:
                    updateF(iLoop, jLoop, xLoop)
                    xLoop -= 1
                jLoop += 1
            iLoop += 1

        forwardMatrix = [[[False] * outerCircle for _ in range(oldScrew + 2)] for _ in range(insideForest + 1)]
        forwardMatrix[insideForest][0][0] = True

        def updateG(i: int, j: int, y: int) -> None:
            forwardMatrix[i - 1][j][y] = forwardMatrix[i - 1][j][y] or forwardMatrix[i][j][y]
            combinedBit2 = y | nums[i - 1]
            forwardMatrix[i - 1][j + 1][combinedBit2] = forwardMatrix[i - 1][j + 1][combinedBit2] or forwardMatrix[i][j][y]

        iCursor = insideForest
        while iCursor >= 1:
            jCursor = 0
            while jCursor <= oldScrew:
                yCursor = outerCircle - 1
                while yCursor >= 0:
                    updateG(iCursor, jCursor, yCursor)
                    yCursor -= 1
                jCursor += 1
            iCursor -= 1

        resultVal = 0
        procI = oldScrew
        while procI <= insideForest - oldScrew:
            procX = 0
            while procX < outerCircle:
                if deltaGraph[procI][oldScrew][procX]:
                    procY = 0
                    while procY < outerCircle:
                        if forwardMatrix[procI][oldScrew][procY]:
                            xorVal = procX ^ procY
                            if xorVal > resultVal:
                                resultVal = xorVal
                        procY += 1
                procX += 1
            procI += 1

        return resultVal