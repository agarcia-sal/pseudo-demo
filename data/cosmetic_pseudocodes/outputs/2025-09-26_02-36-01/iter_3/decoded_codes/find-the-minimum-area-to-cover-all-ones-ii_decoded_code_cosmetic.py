from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        onesCollection = []
        rowIndex = 0
        while rowIndex < len(grid):
            colIndex = 0
            while colIndex < len(grid[rowIndex]):
                if grid[rowIndex][colIndex] == 1:
                    coordinatePair = (rowIndex, colIndex)
                    onesCollection.append(coordinatePair)
                colIndex += 1
            rowIndex += 1

        def rect_area(points):
            if not points:
                return 0

            firstElements = []
            secondElements = []
            idx = 0
            while idx < len(points):
                firstElements.append(points[idx][0])
                secondElements.append(points[idx][1])
                idx += 1

            minRow = firstElements[0]
            maxRow = firstElements[0]
            idx = 1
            while idx < len(firstElements):
                if firstElements[idx] < minRow:
                    minRow = firstElements[idx]
                if firstElements[idx] > maxRow:
                    maxRow = firstElements[idx]
                idx += 1

            minCol = secondElements[0]
            maxCol = secondElements[0]
            idx = 1
            while idx < len(secondElements):
                if secondElements[idx] < minCol:
                    minCol = secondElements[idx]
                if secondElements[idx] > maxCol:
                    maxCol = secondElements[idx]
                idx += 1

            rectWidth = maxRow - minRow + 1
            rectHeight = maxCol - minCol + 1
            return rectWidth * rectHeight

        minimumSumValue = float('inf')
        totalOnes = len(onesCollection)

        firstIdx = 1
        while firstIdx <= totalOnes - 1:
            secondIdx = firstIdx + 1
            while secondIdx <= totalOnes - 1:
                thirdIdx = secondIdx + 1
                while thirdIdx <= totalOnes:
                    allOnesSet = set(onesCollection)
                    combinationsFirst = combinations(onesCollection, firstIdx)
                    for groupOne in combinationsFirst:
                        groupOneSet = set(groupOne)
                        remainingAfterOne = allOnesSet - groupOneSet
                        neededSecondCount = secondIdx - firstIdx
                        if neededSecondCount > len(remainingAfterOne):
                            continue
                        combinationsSecond = combinations(remainingAfterOne, neededSecondCount)
                        for groupTwo in combinationsSecond:
                            groupTwoSet = set(groupTwo)
                            groupThreeSet = remainingAfterOne - groupTwoSet

                            areaOneVal = rect_area(groupOne)
                            areaTwoVal = rect_area(groupTwo)
                            areaThreeVal = rect_area(groupThreeSet)

                            if areaOneVal > 0 and areaTwoVal > 0 and areaThreeVal > 0:
                                combinedSum = areaOneVal + areaTwoVal + areaThreeVal
                                if combinedSum < minimumSumValue:
                                    minimumSumValue = combinedSum
                    thirdIdx += 1
                secondIdx += 1
            firstIdx += 1

        return minimumSumValue