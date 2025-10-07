class Solution:
    def maximumLength(self, nums, k):
        lengthNums = 0
        while lengthNums < len(nums):
            lengthNums += 1

        def initMatrix(rows, cols):
            if rows == 0:
                return []
            else:
                firstRow = []
                colIndex = 0
                while colIndex < cols:
                    firstRow.append(1)
                    colIndex += 1
                return [firstRow] + initMatrix(rows - 1, cols)

        matrixF = initMatrix(lengthNums, k + 1)

        def maxValue(a, b):
            return a if a > b else b

        def innerLoop(currentI, currentH, currentJ):
            if currentJ < 0:
                return
            currentX = nums[currentI]
            currentY = nums[currentJ]
            if currentX == currentY:
                matrixF[currentI][currentH] = maxValue(matrixF[currentI][currentH], matrixF[currentJ][currentH] + 1)
            else:
                if currentH != 0:
                    matrixF[currentI][currentH] = maxValue(matrixF[currentI][currentH], matrixF[currentJ][currentH - 1] + 1)
            innerLoop(currentI, currentH, currentJ - 1)

        def middleLoop(currentI, currentH):
            if currentH > k:
                return
            innerLoop(currentI, currentH, currentI - 1)
            middleLoop(currentI, currentH + 1)

        answer = 0

        def outerLoop(iIndex):
            nonlocal answer
            if iIndex >= lengthNums:
                return
            middleLoop(iIndex, 0)
            if matrixF[iIndex][k] > answer:
                answer = matrixF[iIndex][k]
            outerLoop(iIndex + 1)

        outerLoop(0)

        return answer