class Solution:
    def minimumSum(self, grid):
        infinitePos = (10**9) + (10**9)
        onePositions = []
        rowIdx = 0
        while rowIdx <= len(grid) - 1:
            colIdx = 0
            while True:
                if colIdx > len(grid[rowIdx]) - 1:
                    break
                if grid[rowIdx][colIdx] != 1:
                    colIdx += 1
                    continue
                onePositions.append((rowIdx, colIdx))
                colIdx += 1
            rowIdx += 1

        def rect_area(points):
            if len(points) == 0:
                return 0
            minRow = points[0][0]
            maxRow = points[0][0]
            minCol = points[0][1]
            maxCol = points[0][1]
            idx = 1
            while idx < len(points):
                r, c = points[idx]
                if r < minRow:
                    minRow = r
                if r > maxRow:
                    maxRow = r
                if c < minCol:
                    minCol = c
                if c > maxCol:
                    maxCol = c
                idx += 1
            width = (maxRow - minRow) + 1
            height = (maxCol - minCol) + 1
            return width * height

        minimalSum = infinitePos
        totalOnes = len(onePositions)

        def generateCombinations(collection, size):
            if size == 0:
                return [[]]
            if len(collection) < size:
                return []
            firstElem = collection[0]
            remaining = collection[1:]
            withFirst = generateCombinations(remaining, size - 1)
            for comb in withFirst:
                comb.insert(0, firstElem)
            withoutFirst = generateCombinations(remaining, size)
            return withFirst + withoutFirst

        iVar = 1
        while iVar <= totalOnes - 1:
            jVar = iVar + 1
            while jVar <= totalOnes - 1:
                kVar = jVar + 1
                while kVar <= totalOnes:
                    combosI = generateCombinations(onePositions, iVar)
                    for subsetA in combosI:
                        setOnePositions = {elem: True for elem in onePositions}
                        subsetAMap = {elem: True for elem in subsetA}
                        restAfterA = [elem for elem in onePositions if elem not in subsetAMap]
                        combosJ = generateCombinations(restAfterA, jVar - iVar)
                        for subsetB in combosJ:
                            subsetBMap = {elem: True for elem in subsetB}
                            subsetC = [elem for elem in restAfterA if elem not in subsetBMap]
                            areaA = rect_area(subsetA)
                            areaB = rect_area(subsetB)
                            areaC = rect_area(subsetC)
                            if areaA > 0 and areaB > 0 and areaC > 0:
                                summed = areaA + areaB + areaC
                                if summed < minimalSum:
                                    minimalSum = summed
                    kVar += 1
                jVar += 1
            iVar += 1

        return minimalSum