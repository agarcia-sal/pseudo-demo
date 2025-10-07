class Solution:
    def countSubmatrices(self, grid, k):
        delta = 0
        alpha = len(grid)
        beta = len(grid[0])

        def checkValidity(sub):
            for row in sub:
                for val in row:
                    if val > k:
                        return False
            return True

        def checkSortedness(sub):
            for row in sub:
                for idx in range(1, len(row)):
                    if row[idx] > row[idx - 1]:
                        return False
            return True

        def extractSubmatrix(P, Q, R, S):
            tempMatrix = []
            for idx1 in range(P, R + 1):
                rowSlice = []
                for idx2 in range(Q, S + 1):
                    rowSlice.append(grid[idx1][idx2])
                tempMatrix.append(rowSlice)
            return tempMatrix

        i = 0
        while i <= alpha - 1:
            j = 0
            while j <= beta - 1:
                kVar = i
                while True:
                    if kVar > alpha - 1:
                        break
                    lVar = j
                    while True:
                        if lVar > beta - 1:
                            break
                        curSub = extractSubmatrix(i, j, kVar, lVar)
                        if checkValidity(curSub) and checkSortedness(curSub):
                            delta += 1
                        lVar += 1
                    kVar += 1
                j += 1
            i += 1

        return delta