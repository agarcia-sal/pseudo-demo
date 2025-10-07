from typing import List, Any

class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def addVals(a: int, b: int) -> int:
            return a + b

        def absVal(x: int) -> int:
            if x < 0:
                return -x
            else:
                return x

        def divInt(a: int, b: int) -> int:
            return a // b  # integer division

        def lengthList(lst: List[Any]) -> int:
            countIndex = 0
            while True:
                try:
                    _ = lst[countIndex]
                    countIndex += 1
                except IndexError:
                    break
            return countIndex

        alpha = lengthList(image)
        beta = lengthList(image[0])
        omega: List[List[int]] = []
        phi = 0
        while phi < alpha:
            tmpList = []
            psi = 0
            while psi < beta:
                tmpList.append(0)
                psi += 1
            omega.append(tmpList)
            phi += 1

        gamma: List[List[int]] = []
        delta = 0
        while delta < alpha:
            sigma = []
            tau = 0
            while tau < beta:
                sigma.append(0)
                tau += 1
            gamma.append(sigma)
            delta += 1

        def checkRegion(a: int, b: int) -> bool:
            def adjPairs() -> List[tuple[int, int]]:
                return [(-1, 0), (1, 0), (0, -1), (0, 1)]

            outerX = a
            while outerX < a + 3:
                outerY = b
                while outerY < b + 3:
                    adjIndex = 0
                    adjList = adjPairs()
                    while adjIndex < lengthList(adjList):
                        dx, dy = adjList[adjIndex]
                        nx = outerX + dx
                        ny = outerY + dy
                        if 0 <= nx < a + 3 and 0 <= ny < b + 3:
                            # Since nx, ny, outerX, outerY are all within 3x3 region starting at (a,b),
                            # and image dimensions alpha and beta allow this indexing
                            diff = image[outerX][outerY] - image[nx][ny]
                            if absVal(diff) > threshold:
                                return False
                        adjIndex += 1
                    outerY += 1
                outerX += 1
            return True

        def avgCalc(a: int, b: int) -> int:
            totalSum = 0
            idxX = a
            while idxX < a + 3:
                idxY = b
                while idxY < b + 3:
                    totalSum = addVals(totalSum, image[idxX][idxY])
                    idxY += 1
                idxX += 1
            return divInt(totalSum, 9)

        outerLoop = 0
        while outerLoop < alpha - 2:
            innerLoop = 0
            while innerLoop < beta - 2:
                regionCheck = checkRegion(outerLoop, innerLoop)
                if regionCheck:
                    averageVal = avgCalc(outerLoop, innerLoop)
                    xx = outerLoop
                    while xx < outerLoop + 3:
                        yy = innerLoop
                        while yy < innerLoop + 3:
                            omega[xx][yy] += averageVal
                            gamma[xx][yy] += 1
                            yy += 1
                        xx += 1
                innerLoop += 1
            outerLoop += 1

        p = 0
        while p < alpha:
            q = 0
            while q < beta:
                if gamma[p][q] > 0:
                    omega[p][q] = omega[p][q] // gamma[p][q]
                else:
                    omega[p][q] = image[p][q]
                q += 1
            p += 1

        return omega